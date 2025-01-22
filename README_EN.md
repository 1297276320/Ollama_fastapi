
# Ollama FastAPI Project

This project demonstrates deploying a FastAPI-based service for the Qwen model with Ollama framework, including POST requests and a Gradio interface.

---

## **1. Project Structure**
- **`post_stream.py`**: Sends POST requests and handles streaming responses.
- **`qwen_api.py`**: Implements the FastAPI backend.
- **`qwen_gradio.py`**: Provides a Gradio interface.

---

## **2. Environment Setup**

### **Python and CUDA Requirements**
- **Python Version**: 3.12.3
- **CUDA Version**: 12.4
- **GPU Requirements**: NVIDIA 2080Ti (10GB VRAM or higher recommended)

### **Required Python Libraries**
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

## **3. Deployment Steps**

### **1. Prepare the Environment**
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

## **4. Run Components**
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

## **5. Using Git**
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

If you have any questions, feel free to raise issues in the GitHub repository!
