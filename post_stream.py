import requests
import json

# API URL 和 headers
url = "http://127.0.0.1:10005/generate"  # 根据实际接口地址修改
headers = {
    "accept": "application/json",
    "Authorization": "Bearer your_token_here",  # 如果不需要认证，可以移除
    "Content-Type": "application/json",
}

# 请求数据
data = {
    "prompt": "写一个机器学习的发展史"  # 根据实际需求修改
}

# 使用 stream=True
response = requests.post(url, headers=headers, json=data, stream=True, timeout=(10, 20))

# 检查响应状态
if response.status_code == 200:
    # 初始化拼接文本变量
    combined_text = ""
    try:
        # 流式读取响应内容
        # for chunk in response.iter_lines(decode_unicode=True):# 按行读取，可以取消改为其他的
        for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
            print(chunk, end="", flush=True)
            #print(chunk)
            if chunk:  # 如果有数据
                try:
                    # 如果 chunk 是文本数据，直接拼接
                    combined_text += chunk
                    #print(chunk, end="", flush=True)  # 实时打印到终端
                except json.JSONDecodeError as e:
                    print(f"JSON 解码失败: {e}")
    except KeyboardInterrupt:
        print("\n流式请求已手动中断。")

    # 保存到文件
    with open("流式生成结果.txt", "w", encoding="utf-8") as f:
        f.write(combined_text) 
    print("\n保存成功！")
else:
    print(f"请求失败，状态码: {response.status_code}")
