
# Ollama FastAPI Project

This project demonstrates how to deploy a FastAPI-based API service for interfacing with the Qwen model, integrated with Ollama's framework, and provides various functionalities including POST requests and a user-friendly Gradio interface.

---

## **1. Project Structure**
- **`post_stream.py`**: Sends POST requests to the FastAPI endpoint and handles streaming responses.
- **`qwen_api.py`**: Implements the FastAPI backend for interfacing with the Qwen model.
- **`qwen_gradio.py`**: Provides a Gradio-based interactive web interface for user interactions.

---

## **2. Environment Setup**

### **Python and CUDA Requirements**
- **Python Version**: 3.12.3
- **CUDA Version**: 12.4
- **GPU Requirements**: NVIDIA 2080Ti (10GB VRAM or higher recommended)

### **Required Python Libraries**
Install the dependencies using `requirements.txt` or manually:
```plaintext
fastapi==0.100.0
uvicorn==0.22.0
pydantic==1.10.0
gradio==3.34.0
requests==2.31.0
```
To install, run:
```bash
pip install -r requirements.txt
```

---

## **3. Deployment Steps**

### **1. Preparing the Environment**
1. **Install VS Code Plugins**:
   - Install VS Code and connect to the server via SSH.
   - Synchronize all local plugins with the remote environment.

2. **Set Up Directories**:
   - Create a folder named `ollama_fast` under `/root/`.
   - Use a terminal in Linux to deploy the Ollama framework.

3. **Deploy Ollama**:
   - Download and install the Ollama framework in the folder.
   - Run `ollama serve` to launch the framework (ignore warnings).

4. **Download the Model**:
   - Use Ollama's terminal commands to download the model.
   - After downloading, you can find the model files in `~/.ollama/`.

---

### **2. Running Components**
#### **1. FastAPI Backend**
Run `qwen_api.py` to start the API service:
```bash
python qwen_api.py
```
Once running, the API is available at `http://0.0.0.0:10005`.

#### **2. Sending POST Requests**
Run `post_stream.py` to send requests to the API endpoint:
```bash
python post_stream.py
```
- This script sends a `POST` request with a customizable `prompt`.
- Streams the response and saves it to a file named `流式生成结果.txt`.

#### **3. Gradio Interface**
Run `qwen_gradio.py` to launch the interactive Gradio interface:
```bash
python qwen_gradio.py
```
- This provides a user-friendly interface for interacting with the model.

---

## **4. Using Git**
### **Initial Setup**
1. Configure Git:
   ```bash
   git config --global user.name "Your Username"
   git config --global user.email "Your Email"
   ```

2. Generate and Upload SSH Key:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "Your Email"
   cat ~/.ssh/id_rsa.pub
   ```
   Copy the key and add it to your GitHub account under **Settings > SSH and GPG keys**.

3. Clone or initialize the repository:
   ```bash
   git init
   git remote add origin git@github.com:YourUsername/YourRepository.git
   ```

### **Push Code**
1. Stage, commit, and push:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. For subsequent updates:
   ```bash
   git add .
   git commit -m "Update"
   git push
   ```

---

## **5. Additional Notes**
- Ollama is bandwidth-intensive, especially during model downloads. Use it during low network congestion times for optimal performance.
- GPU resources are used heavily. Ensure sufficient VRAM (10GB or higher recommended).
- Be cautious when editing model-related files; modifying specific parameters can lead to unexpected behavior.

---

# Ollama FastAPI 项目

本项目展示了如何基于 Ollama 框架部署一个基于 Qwen 模型的 FastAPI 服务，并提供多种功能，包括 POST 请求和一个用户友好的 Gradio 界面。

---

## **1. 项目结构**
- **`post_stream.py`**：向 FastAPI 接口发送 POST 请求并处理流式响应。
- **`qwen_api.py`**：实现 Qwen 模型接口的 FastAPI 后端。
- **`qwen_gradio.py`**：提供基于 Gradio 的交互式用户界面。

---

## **2. 环境设置**

### **Python 和 CUDA 要求**
- **Python 版本**：3.12.3
- **CUDA 版本**：12.4
- **GPU 要求**：NVIDIA 2080Ti（推荐 10GB 显存或更高）

### **所需的 Python 库**
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

## **3. 部署步骤**

### **1. 准备环境**
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

### **2. 启动组件**
#### **1. 启动 FastAPI 后端**
运行 `qwen_api.py` 启动 API 服务：
```bash
python qwen_api.py
```
运行后，API 可通过 `http://0.0.0.0:10005` 访问。

#### **2. 发送 POST 请求**
运行 `post_stream.py`，向接口发送请求：
```bash
python post_stream.py
```
- 脚本发送自定义 `prompt` 的 POST 请求。
- 流式响应会保存到文件 `流式生成结果.txt`。

#### **3. 启动 Gradio 界面**
运行 `qwen_gradio.py` 启动交互界面：
```bash
python qwen_gradio.py
```
- 提供便捷的交互式界面，用于与模型交互。

---

## **4. 使用 Git**
### **初始化设置**
1. 配置 Git：
   ```bash
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```

2. 生成并上传 SSH 密钥：
   ```bash
   ssh-keygen -t rsa -b 4096 -C "你的邮箱"
   cat ~/.ssh/id_rsa.pub
   ```
   复制公钥并添加到 GitHub **Settings > SSH and GPG keys** 中。

3. 初始化或克隆仓库：
   ```bash
   git init
   git remote add origin git@github.com:你的用户名/你的仓库名.git
   ```

### **推送代码**
1. 添加、提交并推送：
   ```bash
   git add .
   git commit -m "初始化提交"
   git push -u origin main
   ```

2. 后续更新：
   ```bash
   git add .
   git commit -m "更新描述"
   git push
   ```

---

## **5. 其他注意事项**
- Ollama 在模型下载时会占用大量带宽。建议在网络空闲时使用。
- GPU 资源消耗较高，确保显存满足最低需求（推荐 10GB 或更高）。
- 修改模型相关文件时需小心，错误的更改可能导致意外行为。

---

如果有任何问题，欢迎在 GitHub 仓库提出 issue！
