
# Ollama FastAPI 项目

本项目旨在展示如何基于 Ollama 框架和 Qwen 模型，使用 FastAPI 构建一个高效的接口服务。项目支持发送 POST 请求、流式处理响应，并通过 Gradio 提供用户友好的交互界面。以下为详细说明。

---

## **1. 项目结构**
- **`post_stream.py`**：
  - 用于向 FastAPI 接口发送 POST 请求。
  - 支持流式处理响应，实时显示生成内容，并将最终结果保存到本地文件。
- **`qwen_api.py`**：
  - FastAPI 后端代码，处理客户端请求并与 Qwen 模型交互。
- **`qwen_gradio.py`**：
  - 提供基于 Gradio 的交互界面，方便用户直接使用模型的功能。

---

## **2. 环境要求**

### **2.1 硬件要求**
- **GPU**：NVIDIA 2080Ti（推荐 10GB 显存或更高）。
- **内存**：至少 16GB（推荐 32GB 以上）。
- **存储空间**：至少 50GB 可用空间，用于存储模型及其权重。

### **2.2 软件要求**
- **操作系统**：Linux（Ubuntu 20.04 或以上版本）。
- **Python 版本**：3.12.3。
- **CUDA 版本**：12.4。

### **2.3 所需 Python 库**
项目依赖以下 Python 库，请确保使用 `pip` 安装正确版本：
```plaintext
fastapi==0.100.0
uvicorn==0.22.0
pydantic==1.10.0
gradio==3.34.0
requests==2.31.0
```
安装方式：
```bash
pip install -r requirements.txt
```

---

## **3. 部署步骤**

### **3.1 环境准备**
1. **安装 VS Code 插件**：
   - 使用 SSH 连接服务器。
   - 安装本地 VS Code 的插件后，将其同步到远程服务器。
   - 信任项目文件夹的作者。

2. **创建工作目录**：
   - 在 `/root/` 下新建一个名为 `ollama_fast` 的文件夹，用于存放项目文件。

3. **部署 Ollama 框架**：
   - 使用终端命令下载并安装 Ollama 框架。
   - 启动服务：
     ```bash
     ollama serve
     ```
   - 注意：启动时可能会有显卡相关警告，但实际并不影响运行。

4. **下载模型**：
   - 使用 Ollama 提供的命令下载 Qwen 模型。
   - 下载完成后，模型文件会存储在 `~/.ollama/` 目录下。
     - **`Blobs` 文件夹**：存储二进制模型权重（约 4.36G）。
     - **其他文件**：包含模型的说明与配置。

### **3.2 启动服务**
1. **启动 FastAPI 后端**：
   - 运行以下命令：
     ```bash
     python qwen_api.py
     ```
   - 成功启动后，接口地址为：`http://0.0.0.0:10005`。

2. **发送 POST 请求**：
   - 运行 `post_stream.py`：
     ```bash
     python post_stream.py
     ```
   - 默认情况下，脚本会发送一个带有 `prompt` 的请求，并流式接收模型响应。
   - 生成的内容会保存到 `流式生成结果.txt` 文件中。

3. **启动 Gradio 界面**：
   - 运行 `qwen_gradio.py`：
     ```bash
     python qwen_gradio.py
     ```
   - 启动后，通过生成的链接即可访问交互界面。

---

## **4. 使用 Git 管理代码**

### **4.1 配置 Git**
1. 设置用户名和邮箱：
   ```bash
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```

2. 配置 SSH 密钥：
   - 生成 SSH 密钥：
     ```bash
     ssh-keygen -t rsa -b 4096 -C "你的邮箱"
     ```
   - 查看公钥：
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - 将公钥添加到 GitHub 的 **Settings > SSH and GPG keys** 中。

### **4.2 上传项目到 GitHub**
1. 初始化 Git 仓库：
   ```bash
   git init
   ```

2. 添加远程仓库地址：
   ```bash
   git remote add origin git@github.com:你的用户名/你的仓库名.git
   ```

3. 推送代码到远程：
   ```bash
   git add .
   git commit -m "初始化提交"
   git push -u origin main
   ```

### **4.3 后续更新**
在修改代码后，运行以下命令提交更改：
```bash
git add .
git commit -m "更新描述"
git push
```

---

## **5. 注意事项**
1. **带宽占用**：Ollama 模型下载时会占用大量带宽，建议选择网络空闲时进行下载。
2. **显存需求**：使用时需确保显存充足（推荐 10GB 或更高）。
3. **模型修改**：谨慎编辑模型配置文件，不当的修改可能导致模型异常。

---

如果您有任何问题，欢迎通过 GitHub 提出 issue！
