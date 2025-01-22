from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import subprocess
from typing import Iterator

# 定义请求数据模型
class ModelRequest(BaseModel):
    prompt: str

# 创建 FastAPI 应用
app = FastAPI()

def generate_stream(prompt: str) -> Iterator[str]:
    """
    迭代器生成器，用于流式返回 Ollama 输出，逐字符实时输出。
    """
    try:
        # 调用 Ollama 命令行工具
        process = subprocess.Popen(
            ["ollama", "run", "qwen2.5"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # 启用文本模式
            encoding="utf-8",
            bufsize=0  # 禁用缓冲
        )

        # 写入用户输入的 prompt
        process.stdin.write(prompt)
        process.stdin.close()

        # 实时读取输出
        while True:
            char = process.stdout.read(1)  # 按字符读取
            if char == "" and process.poll() is not None:  # 结束条件
                break
            if char:
                yield char  # 每次返回一个字符

        process.stdout.close()

        # 检查是否有错误
        process.wait()
        if process.returncode != 0:
            error_message = process.stderr.read().strip()
            raise RuntimeError(error_message)

    except Exception as e:
        yield f"Error: {str(e)}\n"


@app.post("/generate")
async def generate_text(request: ModelRequest):
    """
    流式生成文本的 API。
    """
    # 使用 StreamingResponse 返回迭代器的内容
    return StreamingResponse(
        generate_stream(request.prompt),
        media_type="text/plain"  # 数据流是纯文本
    )


# 如果直接运行该脚本，则启动 Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10005)
