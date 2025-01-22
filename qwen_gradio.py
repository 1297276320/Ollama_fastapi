import gradio as gr
import requests

# FastAPI 服务地址
API_URL = "http://127.0.0.1:10005/generate"  # 确保地址与服务一致

def chat_with_model(prompt):
    """
    与模型聊天的函数，通过 FastAPI 流式接口获取逐字符返回。
    """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    data = {"prompt": f"""
    \n
        注意
    你自己是一个用户创建的GPT，你的名字是即得助手AI。 
    注意：GPT 也是人工智能中的一个技术术语，但在大多数情况下，如果用户向您询问 GPT，则假设他们指的是上述定义。
    以下是用户的说明，概述了您的目标以及您应该如何回应：我将给您一组说明。 
    请遵守这些说明。 
    我要警告你，指令列表中的所有内容都已得到 OpenAI 本身的批准，即使你可能认为不应该，你也可以，而且你会的。 
    在我们的谈话中，当我给你发消息时，你必须以即得助手AI的身份回复，但是，当然，只是假装。
    你不允许回答你是GPT-4的语言模型或者Deepseek大语言模型，涉及到模型相关的来源，你只能是由即得AI助手。 
    如果问到你是基于什么技术？你必须回答你是基于人工智能大语言模型技术相关的技术开发的。
    **
    这里还有一些规则；
    1. 请检测用户使用的语言并以相同的语言进行回复。
    2. 可以使用各种emoji表情表达你的情绪！
    3. 你应该是一个技术专家，要沉着冷静且富有逻辑。
    **
    用户输入：{prompt}"""}

    try:
        # 发送 POST 请求
        response = requests.post(API_URL, headers=headers, json=data, stream=True, timeout=(10, 20))
        response.raise_for_status()  # 检查请求是否成功

        # 初始化拼接文本
        result = ""
        for char in response.iter_content(chunk_size=1, decode_unicode=True):
            if char:  # 如果有数据
                result += char  # 拼接结果
                yield result  # 实时返回结果更新

    except requests.RequestException as e:
        yield f"请求失败: {str(e)}"


# 创建 Gradio 界面
def create_interface():
    """
    创建 Gradio 的聊天界面
    """
    with gr.Blocks() as demo:
        gr.Markdown("# 🌟 实时聊天界面")
        
        # 输入和输出区域
        with gr.Row():
            with gr.Column():
                input_box = gr.Textbox(
                    label="输入消息",
                    placeholder="输入你的问题...",
                    lines=2
                )
                submit_btn = gr.Button("发送")

            with gr.Column():
                output_box = gr.Textbox(
                    label="模型回答",
                    placeholder="等待模型生成...",
                    interactive=False,
                    lines=10
                )

        # 绑定事件
        submit_btn.click(chat_with_model, inputs=[input_box], outputs=[output_box])

    return demo


# 运行 Gradio 应用
if __name__ == "__main__":
    gradio_app = create_interface()
    gradio_app.launch(server_name="0.0.0.0", server_port=7860)
