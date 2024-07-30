import gradio as gr
import json
from fuzzywuzzy import process

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
# 创建Gradio界面
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(show_label=False, placeholder="Enter your question here...", lines=10)
            submit_btn = gr.Button("Submit")
            user_output = gr.Text(show_label=False, lines=10)

        # 定义模糊匹配函数
    def fuzzy_match(query):
        questions = [item['instruction'] for item in data]
        match = process.extractOne(query, questions)
        for item in data:
            if item['instruction'] == match[0]:
                return item['output']
    
    submit_btn.click(fuzzy_match, inputs=user_input, outputs=user_output)

# 启动Gradio应用
if __name__ == "__main__":
    demo.launch(
        server_name='0.0.0.0',
        server_port=5009,
        show_api=False,
        share=False,
        allowed_paths=['assets'])
