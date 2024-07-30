import gradio as gr
import json
from fuzzywuzzy import process

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


            # 定义模糊匹配函数
def fuzzy_match(query, history):
    questions = [item['instruction'] for item in data]
    match = process.extractOne(query, questions)
    for item in data:
        if item['instruction'] == match[0]:
            bot_mes = item['output']
    history.append((query, bot_mes))
    return "", history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="testguy", container=True, height=600)
    user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=4, container=False)
    submitBtn = gr.Button("Submit")
    emptyBtn = gr.Button("Clear")
    
    submitBtn.click(
        fuzzy_match, [user_input, chatbot], [user_input, chatbot]
    )
    emptyBtn.click(lambda: None, None, chatbot, queue=False)


# 启动Gradio应用
if __name__ == "__main__":
    demo.launch(
        server_name='0.0.0.0',
        server_port=5009,
        show_api=False,
        share=False,
        allowed_paths=['assets'])
