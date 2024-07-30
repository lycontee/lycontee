import gradio as gr
import json
from fuzzywuzzy import process

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 定义模糊匹配函数
def fuzzy_match(query, history):
    questions = [item['instruction'] for item in data]
    matchs = process.extract(query, questions, limit=5)
    
    index = 1
    match = []
    for t in matchs:
        # 生成序号和匹配项
        match_line = f"{index}: {t[0]}"
        match.append(match_line)
        index += 1
    history.append((query, "\n".join(match)))
    return "", history

# 定义处理用户选择序号的函数
def handle_selection(history, selection):
    if not history:
        return "No previous queries.", history
    
    last_query, matches = history[-1]
    match_lines = matches.split("\n")
    
    try:
        selected_index = int(selection) - 1
        if 0 <= selected_index < len(match_lines):
            selected_match = match_lines[selected_index].split(": ")[1]
            return selected_match, history
        else:
            return f"Invalid selection: {selection}", history
    except ValueError:
        return f"Invalid input: {selection}", history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="testguy", container=True, height=600)

    with gr.Row():
        user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=4, container=False)
        selection_input = gr.Number(label="Select Index", minimum=1, maximum=5, step=1)
        with gr.Column(min_width=10, scale=0.2):
            submitBtn = gr.Button("Submit")
            emptyBtn = gr.Button("Clear")
    
    # 提交按钮点击事件
    submitBtn.click(
        fuzzy_match, [user_input, chatbot], [user_input, chatbot]
    )
    
    # 清空按钮点击事件
    emptyBtn.click(lambda: None, None, chatbot, queue=False)
    
    # 处理用户选择序号的逻辑
    selection_input.change(handle_selection, [chatbot, selection_input], [user_input, chatbot])

# 启动Gradio应用
if __name__ == "__main__":
    demo.launch(
        server_name='0.0.0.0',
        server_port=5009,
        show_api=False,
        share=False,
        allowed_paths=['assets'])
