## 学习资料
- [Custom Components In Five Minutes](https://www.gradio.app/guides/custom-components-in-five-minutes)A

- [一文搞懂模型展示工具Gradio的所有功能 - 知乎](https://zhuanlan.zhihu.com/p/679668818)

- [Gradio入门详细教程_gradio教程-CSDN博客](https://blog.csdn.net/weixin_45277161/article/details/134998849)

- [python fuzzywuzzy模块 模糊字符串匹配详细用法_fuzz.ratio keyerror-CSDN博客](https://blog.csdn.net/sunyao_123/article/details/76942809)

- [240708-Sphinx常用插件整理_sphinx 代码插件-CSDN博客](https://blog.csdn.net/qq_33039859/article/details/140279965)

- [AutoDL私有云初体验 - 知乎](https://zhuanlan.zhihu.com/p/684908968)

- [HF镜像网站](https://hf-mirror.com/)

- [最新开源大语言模型GLM-4模型详细教程—环境配置+模型微调+模型部署+效果展示_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11z421b7f4/?spm_id_from=333.880.my_history.page.click&vd_source=e5f5fb7dfde58880e2a7485fc9f2da4f)

---

## 工具

- [Jupyter Lab登录，密码：aigc.jnw](http://aigc-wenxin:5010/lab/tree/Projetcs)

---

## 测试地址
- http://aigc-wenxin:5009

---

## 示例代码

```python
#%%
import os 
import gradio as gr

# %%
with gr.Blocks() as demo: 
    title = """
    <div style="text-align: center;">
    <h1>💻 Intership: Learning Gradio Component </h1> 
    </div>
    """

    gr.HTML(title)

    
def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet, 
    inputs="textbox", 
    outputs="textbox"
    #可以加title，description来完成标题和概述的编写
)



## 确保程序在5009端口使用
if __name__ == "__main__":
    demo.launch(
        server_name='0.0.0.0',
        server_port=5009,
        show_api=False,
        share=False,
        allowed_paths=['assets'])
```

---


## 组件示例


### 输入组件

1. *Audio*        
   允许用户上传音频文件或直接录音。参数：source: 指定音频来源（如麦克风）、type: 指定返回类型。   
    **示例：gr.Audio(source="microphone", type="filepath")**       
2. *Checkbox*        
   提供复选框，用于布尔值输入。参数：label: 显示在复选框旁边的文本标签。  
    **示例：gr.Checkbox(label="同意条款")**          
3. *CheckboxGroup*            
   允许用户从一组选项中选择多个。参数：choices: 字符串数组，表示复选框的选项、label: 标签文本。  
    **示例：gr.CheckboxGroup(["选项1", "选项2", "选项3"], label="选择你的兴趣")**          
4. *ColorPicker*             
   用于选择颜色，通常返回十六进制颜色代码。参数：default: 默认颜色值。  
    **示例：gr.ColorPicker(default="#ff0000")**     
5. *Dataframe*               
   允许用户上传CSV文件或输入DataFrame。参数：headers: 列标题数组、row_count: 初始显示的行数。  
    **示例：gr.Dataframe(headers=["列1", "列2"], row_count=5)**      
6. *Dropdown*               
   下拉菜单，用户可以从中选择一个选项。参数：choices: 字符串数组，表示下拉菜单的选项、label: 标签文本。  
    **示例：gr.Dropdown(["选项1", "选项2", "选项3"], label="选择一个选项")**     
7. *File*                   
    用于上传任意文件，支持多种文件格式。参数：file_count: 允许上传的文件数量，如"single"或"multiple"、type: 返回的数据类型，如"file"或"auto"。  
    **示例：gr.File(file_count="single", type="file")**      
8. *Image*                      
    用于上传图片，支持多种图像格式。参数：type图像类型，如pil。  
    **示例：gr.Image(type='pil')**       
9. *Number*                    
    数字输入框，适用于整数和浮点数。参数：default: 默认数字、label: 标签文本。  
    **示例：gr.Number(default=0, label="输入一个数字")**      
10. *Radio*                 
    单选按钮组，用户从中选择一个选项。参数：choices: 字符串数组，表示单选按钮的选项、label: 标签文本。  
    **示例：gr.Radio(["选项1", "选项2", "选项3"], label="选择一个选项")**     
11. *Slider*        
    滑动条，用于选择一定范围内的数值。参数：minimum: 最小值、maximum: 最大值、step: 步长、label: 标签文本。  
    **示例：gr.Slider(minimum=0, maximum=10, step=1, label="调整数值")**       
12. *Textbox*                   
    单行文本输入框，适用于简短文本。参数：default: 默认文本、placeholder: 占位符文本。  
    **示例：gr.Textbox(default="默认文本", placeholder="输入文本")**       
13. *Textarea*                           
    多行文本输入区域，适合较长的文本输入。参数：lines: 显示行数、placeholder: 占位符文本。  
    **示例：gr.Textarea(lines=4, placeholder="输入长文本")**        
14. *Time*                      
    用于输入时间。参数：label: 标签文本。  
    **示例：gr.Time(label="选择时间")**        
15. *Video*                         
    视频上传组件，支持多种视频格式。参数：label: 标签文本。  
    **示例：gr.Video(label="上传视频")**              
16. *Data*           
    用于上传二进制数据，例如图像或音频的原始字节。参数：type: 数据类型，如"auto"自动推断。  
    **示例：gr.Data(type="auto", label="上传数据")**        


### 输出组件


1. *Audio*  
    播放音频文件。参数：type 指定输出格式。            
    **示例：gr.Audio(type="auto")**
2. *Carousel*  
    以轮播方式展示多个输出，适用于图像集或多个数据点。参数：item_type 设置轮播项目类型。       
    **示例：gr.Carousel(item_type="image")**
3. *Dataframe*   
    展示Pandas DataFrame，适用于表格数据。参数：type 指定返回的DataFrame类型。     
    **示例：gr.Dataframe(type="pandas")**
4. *Gallery*   
    以画廊形式展示一系列图像。
5. *HTML*   
    展示HTML内容，适用于富文本或网页布局。
6. *Image*  
    展示图像。参数：type 指定图像格式。          
    **示例：gr.Image(type="pil")**
7. *JSON*  
    以JSON格式展示数据，便于查看结构化数据。
8. *KeyValues*  
    以键值对形式展示数据。
9. *Label*  
    展示文本标签，适用于简单的文本输出。
10. *Markdown*  
    支持Markdown格式的文本展示。
11. *Plot*  
    展示图表，如matplotlib生成的图表。
12. *Text*  
    用于显示文本，适合较长的输出。
13. *Video*  
    播放视频文件。


### 实例代码
```bash
import gradio as gr
 
# 定义一个处理多种 Gradio 输入组件值的函数
def greet(textbox, dropdown, radio, checkbox, slider, image, audio, video, file, number, dataframe, color):
    # 创建一个包含用户选择的字符串
    output_text = f"您选择了：{textbox}，{dropdown}，{radio}，{checkbox}，滑块值：{slider}，数字：{number}，颜色：{color}"
    # 创建一个包含用户选择的 Markdown 字符串（加粗文本）
    output_markdown = f"**您选择了**：{textbox}，{dropdown}，{radio}，{checkbox}，滑块值：{slider}，数字：{number}，颜色：{color}"
    # 创建一个包含用户输入选项的 JSON 字典
    output_json = {
        "textbox": textbox,
        "dropdown": dropdown,
        "radio": radio,
        "checkbox": checkbox,
        "slider": slider,
        "number": number,
        "color": color
    }
 
    # 保存图像（如果提供了输入图像）
    output_image = None
    if image is not None:
        output_image = "output_image.png"
        image.save(output_image)
 
    # 保存音频（如果提供了输入音频）
    output_audio = None
    if audio is not None:
        output_audio = "output_audio.wav"
        with open(output_audio, "wb") as f:
            f.write(audio)
 
    # 保存视频（如果提供了输入视频）
    output_video = None
    if video is not None:
        output_video = "output_video.mp4"
        with open(output_video, "wb") as f:
            f.write(video)
 
    # 保存文件（如果提供了输入文件）
    output_file = None
    if file:
        output_file = 'example_output.txt'
        with open(output_file, 'w') as f:
            f.write(output_text)
 
    # 处理数据框（如果提供了输入数据框）
    output_dataframe = None
    if dataframe is not None:
        output_dataframe = dataframe.to_html(index=False)
 
    # 返回颜色
    output_color = "您选择的颜色是：{color}"
 
    # 返回处理后的各种输出组件值
    return None, output_text, None, output_markdown, output_image, output_audio, output_json, output_file, output_video, output_dataframe, output_color
 
# 创建一个 Gradio Interface 实例，包含多个输入和输出组件
iface2 = gr.Interface(
    greet,
    [
        gr.Textbox(lines=2, placeholder="请输入文本…"),
        gr.Dropdown(choices=["选项A", "选项B", "选项C"]),
        gr.Radio(choices=["选项1", "选项2", "选项3"]),
        gr.Checkbox(label="选择此选项"),
        gr.Slider(minimum=10, maximum=90),
        gr.Image(shape=(100, 100)),
        gr.Audio(),
        gr.Video(),
        gr.File(),
        gr.Number(),
        gr.Dataframe(headers=["列A", "列B", "列C"]),
        gr.ColorPicker(),  # 添加颜色选择器输入组件
    ],
    outputs=[
        gr.Textbox(),
        gr.Textbox(),
        gr.Textbox(),
        gr.Markdown(),
        gr.Image(),
        gr.Audio(),
        gr.Json(),
        gr.File(),
        gr.Video(),
        gr.HTML(),
        gr.Textbox(),  # 添加新的输出组件
    ],
    title="Gradio 示例",
    description="这是一个 Gradio 示例应用。",
    examples=[
        [
            "您好",
            "选项A",
            "选项1",
            True,
            25,
            "path/to/image.png",
            "path/to/audio.wav",
            "path/to/video.mp4",
            "path/to/file.txt",
            42,
            [
                ["值A1", "值B1", "值C1"],
                ["值A2", "值B2", "值C2"],
            ],
            "#FF0000",  # 颜色选择器示例值
        ]
    ],
).launch()

```

---

## Conda环境查看、激活与退出
```bash
(intership)[jnw@PPSE1LLM143 Projetcs]$ conda activate intership
(intership)[jnw@PPSE1LLM143 Projetcs]$ conda info -e
# conda environments:
#
intership             *  /home/jnw/.conda/envs/intership
base                     /opt/miniconda3
ChuanhuChat              /opt/miniconda3/envs/ChuanhuChat
dbgpt_hub_lc             /opt/miniconda3/envs/dbgpt_hub_lc
test02                   /opt/miniconda3/envs/test02
testLangChain            /opt/miniconda3/envs/testLangChain
visgpu                   /opt/miniconda3/envs/visgpu
wenxin-doc               /opt/miniconda3/envs/wenxin-doc

(intership)[jnw@PPSE1LLM143 Projetcs]$ conda deactivate
[jnw@PPSE1LLM143 Projetcs]$ conda activate intership
(intership)[jnw@PPSE1LLM143 ~]$ cd Projetcs/
(intership)[jnw@PPSE1LLM143 Projetcs]$ python test_gradio1.py 
Running on local URL:  http://0.0.0.0:5009

To create a public link, set `share=True` in `launch()`.           
```
*进入文件夹 cd ”path“,返回主文件夹 cd*

---

## GLM-4模型
本体在*basic_demo*中，    
需要先将模型的地址传入代码中，   
位置为：**line30** 
```bash
os.environ.get('MODEL_PATH', '/sota/sota_models/glm-4-9b-chat')
```
其中的web_demo，对于gradio配置的网页端文件：*trans_web_demo*，配置网路端口后，启用热重载模式运行
**对于其中模型finetune，可以选用自带的lora，但由于llama可视化优点，我会选择使用它。(注意配置网路端口）**

---
      
### 关于LLaMA可视化网页配置所涉及的域名修改        
需要到main/src/llamafactory/webui中找到interface.py , 并修改最后两部分中的servername以及serverport：     
```bash
def run_web_ui() -> None:
    gradio_share = os.environ.get("GRADIO_SHARE", "0").lower() in ["true", "1"]
    server_name = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")
    create_ui().queue().launch(share=gradio_share, server_name=server_name, server_port=5009, inbrowser=True)


def run_web_demo() -> None:
    gradio_share = os.environ.get("GRADIO_SHARE", "0").lower() in ["true", "1"]
    server_name = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")
    create_web_demo().queue().launch(share=gradio_share, server_name=server_name, server_port=5009, inbrowser=True)
```

---

### 关于json文件        
    换行是\n,键值对,值的格式跟c一样,是用于储存数据的     
    格式为:     
    [     
      {              
      ""="",              
      ""="",              
      ""=""              
      },               
      ……               
    ]

#### python 模块

**导入json  >>>    import  json**

```python
json.loads()    #字符串加载

json.load()     #文件加载

#示例如下

#示例数据:

[
    {
        "name":"Alice",
        "age":30,
        "address":{
            "city":"neverland",
            "postcode":"12345"            
        }
        ...
    }

#文件读取json：
with open('data.json','r') as file:
    data = json.load(file)

#提取数据
name = data['name']
age = data['age']
city = data['address']['city']
...

#展示数据
print(f"Name:{name}")
...


```

---

## the fuzz 模糊匹配   

#### 第一部分

**>>> from fuzzywuzzy import fuzz**            
**>>> from fuzzywuzzy import process**         
```shell

[1]>>> fuzz.ratio("this is a test", "this is a test!")
out    97
是对字段的全匹配，对顺序敏感

[2]>>> fuzz.partial_ratio("this is a test", "this is a test!")
out    100
是对字段的模糊匹配，对顺序敏感

```

#### 第二部分

```shell

[3]>>> fuzz._process_and_sort(s, force_ascii, full_process=True)
对字符串s排序

force_ascii(TF)
T 转换为ascii码

full_process(TF)
T utils.full_process()：将s转小写，去除字母和数字以外字符（不包含-），剩下字符串用space分割，再进行排序。
F 直接对s排序


[4]>>> fuzz._token_sort(s1, s2, partial=True, force_ascii=True, full_process=True)
给出s1,s2两者相似度

是首先函数[3]处理c,
当partial 为T 时，再函数[2]处理；
当partial 为F 时，再函数[1]处理。



[5]>>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
out    100
partial=F 时的函数[4]
对顺序不敏感


[6]>>> fuzz.partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True)
partial=T 时的函数[4]
对顺序不敏感
```

#### 第三部分

```shell

[7]>>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
out    100
较函数[5]忽略了重复单词
对顺序不敏感


[8]>>> fuzz._token_set(s1, s2, partial=True, force_ascii=True, full_process=True)
当partial= F 时，与函数[7]相同


[9]>>> fuzz.partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True)
当partial= T 时，与函数[8]相同
```

#### 第四部分

```shell

[10]>>> fuzz.QRatio(s1, s2, force_ascii=True, full_process=True)
当full_process=T 时，utils.full_process()：先将字符串s转换为小写，去掉除字母和数字之外的字符（发现不能去掉-字符），剩下的字符串以空格分开，然后排序。再函数[1]处理，对顺序敏感


[11]>>> fuzz.UQRatio(s1, s2, full_process=True)
force_ascii= F时的函数[10]


[12]>>> fuzz.WRatio(s1, s2, force_ascii=True, full_process=True)
另一种不同算法计算相似度，对顺序敏感


[13]>>> UWRatio(s1, s2, full_process=True)
force_ascii= F 时的函数[12]
```

#### 第五部分

### 部分总结
    如果计算相似度的字符串只有字母和数字，直接可以用函数[1]ratio（）和函数[2]partial_ratio()。   
       
    但如果还有其他字符，而且我们想要去掉这些没用字符，就用下边的。   
       
    下边的函数都对顺序不敏感，但函数[5]token_sort_ratio（）系列是全字符匹配，不管顺序。   
       
    而函数[7]token_set_ratio（）只要第二个字符串包含第一个字符串就100,不管顺序。
    

#### 第六部分

```shell

EXAMPLE：

>>> choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
>>> process.extract("new york jets", choices, limit=2)
    [('New York Jets', 100), ('New York Giants', 78)]
>>> process.extractOne("cowboys", choices)
    ("Dallas Cowboys", 90)


[14]>>> process.extract(query, choices, processor=default_processor, scorer=default_scorer, limit=5)
query 是字符串
choices 是列表，列表元素 是字符串
processor 是对输入比较的字符串的处理函数，默认是fuzzywuzzy.utils.full_process()：先将字符串s转换为小写，去掉除字母和数字之外的字符（发现不能去掉-字符），剩下的字符串以空格分开，然后排序
scorer 是计算两个字符串相似度的函数，默认为函数[12]
limit 是输出元素个数
extract之后的数据类型是列表，即使limit=1，最后还是列表，注意和下面extractOne的区别
输出为列表，元素为元组，元组第一个匹配到的为str，第二个匹配到的为int（score）
对于输出:按照score排序


[15]>>> process.extractWithoutOrder(query, choices, processor=default_processor, scorer=default_scorer, score_cutoff=0)
score_cutoff 为一个阈值, 当score小于该阈值时，不会输出。返回一个生成器，输出每个大于 score_cutoff的匹配，按顺序输出，不排序。


[16]>>> process.extractBests(query, choices, processor=default_processor, scorer=default_scorer, score_cutoff=0, limit=5)
函数[16]和函数[14]都调用了函数[15]，只不过函数[16]能传输 score_cutoff。


[17]>>> process.extractOne(query, choices, processor=default_processor, scorer=default_scorer, score_cutoff=0)
也调用了函数[15]，能传输score_cutoff,只不过只输出一个score最高的值


[18]>>> process.dedupe(contains_dupes, threshold=70, scorer=fuzz.token_set_ratio)
contains_dupes 是列表，列表元素 为字符串。
取出相似度小于 threshold 的字符串，相似度大于 threshold 的字符串取最长一个。


```


#### 我的实操

**数据示例：**
```json


[
  {
    "instruction": "外部发过来的邮件被拦截怎么办？",
    "input": "",
    "output": "您可以参考以下步骤申请释放邮件：\n1、打开IT Service Request：http://eas1prd2:8029/isrs/is/createRequest.action。\n2、Problem Type选择：E-mail。\n3、Request Ticket Type选择：Email Release。\n4、Descriptions填写申请理由，点击“Submit”。\n5、待签核完毕后，我们会为您释放被拦截的邮件。如果邮件本身携带有病毒，我们将无法给您释放。"
  },
  {
    "instruction": "Outlook打不开，一直正在启动，请问如何处理？",
    "input": "",
    "output": "出现以上问题，您可以参考以下步骤处理：\n1、关闭Outlook。\n2、按住键盘Ctrl键不放，双击Outlook，直到提示“按住CTRL键。是否要在安全模式中启动Outlook”后，松开Ctrl键，点击“是”。\n3、在选择配置文件界面，点击“是”。\n4、正常打开Outlook后，关闭Outlook。之后您可以正常打开Outlook。"
  }
]


```


**函数示例：**
```python


# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
# 定义模糊匹配函数
def fuzzy_match(query):
    questions = [item['instruction'] for item in data]
    match = process.extractOne(query, questions)
    for item in data:
        if item['instruction'] == match[0]:
            return item['output']


```

### 调用ollama
```bash
[jnw@PPSE1LLM143 Projetcs]$ ollama list
NAME                                    ID              SIZE    MODIFIED    
qwen2:72b                               14066dfa503f    41 GB   6 hours ago
mannix/defog-llama3-sqlcoder-8b:latest  9bbf2be085b0    4.7 GB  6 hours ago
deepseek-coder-v2:16b                   8577f96d693e    8.9 GB  6 hours ago
llama3.1:70b                            d729c66f84de    39 GB   6 hours ago
qwen2:0.5b                              6f48b936a09f    352 MB  6 hours ago
qwen2:1.5b                              f6daf2b25194    934 MB  6 hours ago
[jnw@PPSE1LLM143 Projetcs]$ ollama run qwen2:72b
>>> /bye
```
