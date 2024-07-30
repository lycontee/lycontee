import os
from pathlib import Path
from threading import Thread
from typing import Union
import gradio as gr
import torch
from peft import AutoPeftModelForCausalLM, PeftModelForCausalLM

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    PreTrainedTokenizerFast,
    StoppingCriteria,
    StoppingCriteriaList,
    TextIteratorStreamer
)

ModelType = Union[PreTrainedModel, PeftModelForCausalLM]
TokenizerType = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]

MODEL_PATH = os.environ.get('MODEL_PATH', '/sota/sota_models/glm-4-9b-chat')
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)


def _resolve_path(path: Union[str, Path]) -> Path:
    return Path(path).expanduser().resolve()


def load_model_and_tokenizer(
        model_dir: Union[str, Path], trust_remote_code: bool = True
) -> tuple[ModelType, TokenizerType]:
    model_dir = _resolve_path(model_dir)
    if (model_dir / 'adapter_config.json').exists():
        model = AutoPeftModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model.peft_config['default'].base_model_name_or_path
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_dir, trust_remote_code=trust_remote_code, device_map='auto'
        )
        tokenizer_dir = model_dir
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_dir, trust_remote_code=trust_remote_code, use_fast=False
    )
    return model, tokenizer


model, tokenizer = load_model_and_tokenizer(MODEL_PATH, trust_remote_code=True)


class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = model.config.eos_token_id
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False


def parse_text(text):
    lines = text.split("\n")
    lines = [line for line in lines if line != ""]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            items = line.split('`')
            if count % 2 == 1:
                lines[i] = f'<pre><code class="language-{items[-1]}">'
            else:
                lines[i] = f'<br></code></pre>'
        else:
            if i > 0:
                if count % 2 == 1:
                    line = line.replace("`", "\`")
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp;")
                    line = line.replace("*", "&ast;")
                    line = line.replace("_", "&lowbar;")
                    line = line.replace("-", "&#45;")
                    line = line.replace(".", "&#46;")
                    line = line.replace("!", "&#33;")
                    line = line.replace("(", "&#40;")
                    line = line.replace(")", "&#41;")
                    line = line.replace("$", "&#36;")
                lines[i] = "<br>" + line
    text = "".join(lines)
    return text


def predict(history, prompt):
    stop = StopOnTokens()
    messages = []
    if prompt:
        messages.append({"role": "system", "content": prompt})
    for idx, (user_msg, model_msg) in enumerate(history):
        if prompt and idx == 0:
            continue
        if idx == len(history) - 1 and not model_msg:
            messages.append({"role": "user", "content": user_msg})
            break
        if user_msg:
            messages.append({"role": "user", "content": user_msg})
        if model_msg:
            messages.append({"role": "assistant", "content": model_msg})

    model_inputs = tokenizer.apply_chat_template(messages,
                                                 add_generation_prompt=True,
                                                 tokenize=True,
                                                 return_tensors="pt").to(next(model.parameters()).device)
    streamer = TextIteratorStreamer(tokenizer, timeout=60, skip_prompt=True, skip_special_tokens=True)
    generate_kwargs = {
        "input_ids": model_inputs,
        "streamer": streamer,
        "do_sample": True,
        "stopping_criteria": StoppingCriteriaList([stop]),
        "repetition_penalty": 1.2,
        "eos_token_id": model.config.eos_token_id,
    }
    t = Thread(target=model.generate, kwargs=generate_kwargs)
    t.start()
    for new_token in streamer:
        if new_token:
            history[-1][1] += new_token
        yield history


with gr.Blocks() as demo:
    gr.HTML("""<h1 align="center">test</h1>""")
    chatbot = gr.Chatbot(label="testguy", container=True, height=550)

    def set_prompt(prompt_text):
        return [[parse_text(prompt_text), f"那么{prompt_text}"]]

    def user(query, history):
        return "", history + [[parse_text(query), ""]]

    def update(choice):
        if choice == "text":
            return gr.update(visible=False)
        else:
            return gr.update(visible=True)

    def update_2(choice):
        if choice == "text":
            return gr.update(visible=False)
        else:
            return gr.update(visible=True)

    def vote(data: gr.LikeData):
        if data.liked:
            print("You upvoted this response: " + data.value)
        else:
            print("You downvoted this response: " + data.value)

    with gr.Row():
        user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=4, container=False)
        with gr.Column(min_width=10, scale=0.2):
            submitBtn = gr.Button("Submit")
            emptyBtn = gr.Button("Clear")

    with gr.Row():
        with gr.Column(min_width=15, scale=2):
            prompt_input = gr.Textbox(show_label=False, scale=50, interactive=True, visible=False, container=False, lines=4, placeholder="Input...")
        with gr.Column(min_width=5, scale=0.2):
            Dpd = gr.Dropdown(['text','prompt'], value='text', container=False, interactive=True, label="choose the mode")
            promptBtn = gr.Button(value="Submit", visible=False)

    Dpd.change(update, inputs=Dpd, outputs=prompt_input)

    Dpd.change(update, inputs=Dpd, outputs=promptBtn)

    submitBtn.click(user, [user_input, chatbot], [user_input, chatbot], queue=False).then(
        predict, [chatbot, prompt_input], chatbot
    )
    emptyBtn.click(lambda: (None, None), None, [chatbot, prompt_input], queue=False)

    promptBtn.click(set_prompt, inputs=[prompt_input], outputs=chatbot)

    chatbot.like(vote, None, None) 

demo.queue()
# demo.launch(server_name="127.0.0.1", server_port=8000, inbrowser=True, share=True)
if __name__ == "__main__":
    demo.launch(
        server_name='0.0.0.0',
        server_port=5009,
        share=False,
        show_api=False,
        allowed_paths=['assets'])
