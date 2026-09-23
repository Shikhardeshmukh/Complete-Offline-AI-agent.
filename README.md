# Offline AI Assistant 🤖

A privacy-focused AI assistant that runs completely locally on your computer using **Python, Ollama, and Qwen3**. The application does not require paid APIs or an internet connection after the AI model is downloaded.

## 🚀 Features

* 💬 Local AI chat using Qwen3
* 🔒 Completely offline AI inference
* 📝 Create and manage personal notes
* 📄 Summarize local text files
* ⚡ Fast local responses
* 💰 No API costs
* 🌐 No external AI services required

## 🛠️ Tech Stack

* Python
* Ollama
* Qwen3 4B
* File Handling
* Local Storage

## ⚙️ How It Works

The application sends user prompts directly to a locally running **Qwen3 language model through Ollama**. Since the model runs on the user's machine, conversations and local files remain on the computer instead of being sent to a cloud AI service.

## ▶️ Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama pull qwen3:4b
python app.py
```

## 📌 Available Commands

```text
/help
/note <text>
/notes
/summarize <file>
/clear
/exit
```

## 🎯 Project Goal

The goal of this project is to demonstrate how modern **local LLMs and AI agents** can be integrated into Python applications while maintaining privacy, reducing API costs, and enabling AI functionality without cloud dependencies.

## 📈 Future Improvements

* PDF document analysis
* Conversation memory
* Local RAG system
* Voice input and output
* Web-based UI
* Local database integration
* Tool calling and autonomous task execution

---

**Built with Python + Ollama + Qwen3.**
