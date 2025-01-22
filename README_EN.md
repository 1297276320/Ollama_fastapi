
# Ollama FastAPI Project

This project demonstrates how to deploy a FastAPI-based service integrated with the Qwen model and Ollama framework. It supports sending POST requests, streaming responses, and provides a user-friendly interface using Gradio. Below are the detailed instructions.

---

## **1. Project Structure**
- **`post_stream.py`**:
  - Sends POST requests to the FastAPI endpoint.
  - Supports streaming responses, displaying real-time generated content, and saving the final result to a local file.
- **`qwen_api.py`**:
  - Implements the FastAPI backend for handling client requests and interacting with the Qwen model.
- **`qwen_gradio.py`**:
  - Provides an interactive Gradio interface for easier access to the model's functionalities.

---

## **2. Environment Requirements**

### **2.1 Hardware Requirements**
- **GPU**: NVIDIA 2080Ti (10GB VRAM or higher recommended).
- **Memory**: At least 16GB (32GB or more recommended).
- **Storage**: Minimum 50GB of free space for model and weights storage.

### **2.2 Software Requirements**
- **Operating System**: Linux (Ubuntu 20.04 or later).
- **Python Version**: 3.12.3.
- **CUDA Version**: 12.4.

### **2.3 Required Python Libraries**
The following Python libraries are required. Ensure you install the correct versions using `pip`:
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

### **3.1 Preparing the Environment**
1. **Install VS Code Plugins**:
   - Connect to the server via SSH using VS Code.
   - Install your local VS Code plugins and sync them to the remote server.
   - Trust the project folder's author.

2. **Create the Working Directory**:
   - Create a folder named `ollama_fast` under `/root/` to store the project files.

3. **Deploy the Ollama Framework**:
   - Download and install the Ollama framework using terminal commands.
   - Start the service:
     ```bash
     ollama serve
     ```
   - Note: Warnings about GPU detection can be ignored as they do not impact functionality.

4. **Download the Model**:
   - Use Ollama commands to download the Qwen model.
   - After downloading, the model files will be stored in the `~/.ollama/` directory:
     - **`Blobs` folder**: Contains binary model weights (approximately 4.36GB).
     - **Other files**: Include model descriptions and configurations.

### **3.2 Running the Components**
1. **Start the FastAPI Backend**:  
   - Run the following command:  
     ```bash
     python qwen_api.py
     ```
   - The API will be available at: `http://0.0.0.0:10005`.

2. **Send POST Requests**:  
   - Run `post_stream.py`:  
     ```bash
     python post_stream.py
     ```
   - By default, the script sends a `prompt` in the request and streams the model's response.
   - The generated content will be saved in the file `streamed_results.txt`.

3. **Launch the Gradio Interface**:  
   - Run `qwen_gradio.py`:  
     ```bash
     python qwen_gradio.py
     ```
   - Once started, access the interactive interface through the generated link.

---

## **4. Using Git for Version Control**

### **4.1 Configuring Git**
1. Set your Git username and email:  
   ```bash
   git config --global user.name "Your Username"
   git config --global user.email "Your Email"
   ```

2. Configure SSH Keys:  
   - Generate an SSH key:  
     ```bash
     ssh-keygen -t rsa -b 4096 -C "Your Email"
     ```
   - View the public key:  
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Add the public key to GitHub under **Settings > SSH and GPG keys**.

### **4.2 Pushing the Project to GitHub**
1. Initialize the Git repository:  
   ```bash
   git init
   ```

2. Add the remote repository:  
   ```bash
   git remote add origin git@github.com:YourUsername/YourRepository.git
   ```

3. Push your code to the repository:  
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

### **4.3 Updating the Repository**
After making changes to the project, update the repository using the following commands:
```bash
git add .
git commit -m "Update description"
git push
```

---

## **5. Notes**
1. **Bandwidth Usage**: Downloading the Ollama model consumes significant bandwidth. Perform downloads during off-peak hours for better performance.
2. **VRAM Requirements**: Ensure sufficient VRAM (10GB or higher recommended) for optimal performance.
3. **Model Modifications**: Be cautious when editing model configuration files, as incorrect changes can lead to unexpected behavior.

---

If you have any questions, feel free to raise an issue on the GitHub repository!
