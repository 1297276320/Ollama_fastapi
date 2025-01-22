
# Ollama FastAPI 项目

<div id="language-selector">
  <button onclick="switchLanguage('cn')">中文</button>
  <button onclick="switchLanguage('en')">English</button>
</div>

<div id="content-cn" style="display:block;">

## Ollama FastAPI 项目

本项目展示了如何基于 Ollama 框架部署一个基于 Qwen 模型的 FastAPI 服务，并提供多种功能，包括 POST 请求和一个用户友好的 Gradio 界面。

---

### **1. 项目结构**
- **`post_stream.py`**：向 FastAPI 接口发送 POST 请求并处理流式响应。
- **`qwen_api.py`**：实现 Qwen 模型接口的 FastAPI 后端。
- **`qwen_gradio.py`**：提供基于 Gradio 的交互式用户界面。

---

### **2. 环境设置**

#### **Python 和 CUDA 要求**
- **Python 版本**：3.12.3
- **CUDA 版本**：12.4
- **GPU 要求**：NVIDIA 2080Ti（推荐 10GB 显存或更高）

#### **所需的 Python 库**
使用 `requirements.txt` 或手动安装以下依赖：
```plaintext
fastapi==0.100.0
uvicorn==0.22.0
pydantic==1.10.0
gradio==3.34.0
requests==2.31.0
```
安装命令：
```bash
pip install -r requirements.txt
```

---

### **3. 部署步骤**

#### **1. 准备环境**
1. **安装 VS Code 插件**：
   - 安装 VS Code 并通过 SSH 连接到服务器。
   - 同步所有本地插件到远程环境。

2. **设置目录**：
   - 在 `/root/` 下创建名为 `ollama_fast` 的文件夹。
   - 使用 Linux 终端部署 Ollama 框架。

3. **部署 Ollama**：
   - 下载并安装 Ollama 框架。
   - 运行 `ollama serve` 启动框架（忽略警告）。

4. **下载模型**：
   - 使用 Ollama 终端命令下载模型。
   - 下载完成后，模型文件位于 `~/.ollama/`。

---

#### **2. 启动组件**
1. 启动 FastAPI 后端：
   ```bash
   python qwen_api.py
   ```
   接口地址：`http://0.0.0.0:10005`

2. 发送 POST 请求：
   ```bash
   python post_stream.py
   ```
   流式响应会保存到文件 `流式生成结果.txt`。

3. 启动 Gradio 界面：
   ```bash
   python qwen_gradio.py
   ```

---

#### **3. 使用 Git**
1. 配置 Git：
   ```bash
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```
2. 上传代码：
   ```bash
   git add .
   git commit -m "初始化提交"
   git push -u origin main
   ```

---

</div>

<div id="content-en" style="display:none;">

## Ollama FastAPI Project

This project demonstrates deploying a FastAPI-based service for the Qwen model with Ollama framework, including POST requests and a Gradio interface.

---

### **1. Project Structure**
- **`post_stream.py`**: Sends POST requests and handles streaming responses.
- **`qwen_api.py`**: Implements the FastAPI backend.
- **`qwen_gradio.py`**: Provides a Gradio interface.

---

### **2. Environment Setup**

#### **Python and CUDA Requirements**
- **Python Version**: 3.12.3
- **CUDA Version**: 12.4
- **GPU Requirements**: NVIDIA 2080Ti (10GB VRAM or higher recommended)

#### **Required Python Libraries**
Install dependencies using `requirements.txt` or manually:
```plaintext
fastapi==0.100.0
uvicorn==0.22.0
pydantic==1.10.0
gradio==3.34.0
requests==2.31.0
```
Installation command:
```bash
pip install -r requirements.txt
```

---

### **3. Deployment Steps**

#### **1. Prepare the Environment**
1. **Install VS Code Plugins**:
   - Install VS Code and connect to the server via SSH.
   - Synchronize all local plugins with the remote environment.

2. **Set Up Directories**:
   - Create a folder named `ollama_fast` under `/root/`.
   - Use Linux terminal to deploy Ollama framework.

3. **Deploy Ollama**:
   - Download and install the Ollama framework.
   - Run `ollama serve` to start the framework (ignore warnings).

4. **Download the Model**:
   - Use Ollama terminal commands to download the model.
   - After downloading, model files are located in `~/.ollama/`.

---

#### **2. Run Components**
1. Start FastAPI Backend:
   ```bash
   python qwen_api.py
   ```
   API address: `http://0.0.0.0:10005`

2. Send POST Requests:
   ```bash
   python post_stream.py
   ```
   Streamed responses will be saved to `streamed_results.txt`.

3. Start Gradio Interface:
   ```bash
   python qwen_gradio.py
   ```

---

#### **3. Using Git**
1. Configure Git:
   ```bash
   git config --global user.name "Your Username"
   git config --global user.email "Your Email"
   ```
2. Push Code:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

---

</div>

<script>
function switchLanguage(lang) {
  document.getElementById('content-cn').style.display = lang === 'cn' ? 'block' : 'none';
  document.getElementById('content-en').style.display = lang === 'en' ? 'block' : 'none';
}
</script>
