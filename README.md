# AI-Chat-Box-Using-LLM-with-AI-model---Python-Project

# 🤖 AI Chat Box — NeoBot

**NeoBot** is a simple AI-powered chatbot built using Python and the Groq API. It allows users to interact with an AI assistant through a command-line interface and receive concise, conversational responses.

This project demonstrates how to integrate a Large Language Model (LLM) into a Python application using the OpenAI Python SDK and Groq's API.

## 🚀 Features

* **AI-Powered Conversations:** Generate responses using an LLM hosted by Groq.
* **Interactive Chat Interface:** Ask questions directly through the terminal.
* **Conversation Context:** Maintains conversation history during the current session.
* **Custom AI Personality:** Configured to respond as NeoBot with short, concise answers.
* **Environment Variable Security:** Loads the API key from a `.env` file.
* **Exit Command:** Type `q` to quit the chat.

## 🛠️ Technologies Used

* Python
* Groq API
* OpenAI Python SDK
* python-dotenv
* Large Language Models (LLMs)

## 📁 Project Structure

```text
AI-Chat-Box/
│
├── AI_Chat_Box.py    # Main chatbot application
├── .env              # API key configuration (not uploaded)
├── .gitignore        # Files excluded from Git
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Chat-Box.git
```

Navigate to the project directory:

```bash
cd AI-Chat-Box
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure the API Key

Create a `.env` file in the project root directory and add your Groq API key:
Use this link: (https://console.groq.com/home?utm_source=website&utm_medium=outbound_link&utm_campaign=dev_console_click) OR (https://groq.com/). *Need to login, then you get the API KEY*

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Security note:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
python AI_Chat_Box.py
```

## 💬 How to Use

1. Start the application.
2. Enter your question when prompted.
3. NeoBot generates an AI response in the terminal.
4. Continue asking questions within the same session.
5. Type `q` to exit the application.

Example interaction:

```text
Your Question: Hello!
AI: Hello! I'm NeoBot. How can I help you today?

Your Question: What is Python?
AI: Python is a versatile programming language used for
web development, automation, data analysis, and AI.

Your Question: q
```

*Note: The example responses are illustrative. Actual responses depend on the model.*

## 🧠 How It Works

1. **Environment Configuration:** Loads the Groq API key from the `.env` file.
2. **API Initialization:** Creates an API client using the OpenAI Python SDK configured with Groq's API endpoint.
3. **Conversation Management:** Stores system instructions and conversation messages in a list.
4. **Response Generation:** Sends conversation history to the configured `openai/gpt-oss-120b` model.
5. **Interactive Loop:** Accepts user questions continuously and displays the AI-generated responses.

## 🔐 Environment Variables

| Variable       | Description                                   |
| -------------- | --------------------------------------------- |
| `GROQ_API_KEY` | API key used to authenticate requests to Groq |

## 📌 Future Improvements

* Add a graphical user interface (GUI) or web interface.
* Improve exception handling for API errors and network issues.
* Add a conversation reset feature.
* Support streaming responses for faster perceived output.
* Add conversation history export.
* Improve input validation and exit handling.

## 🎯 Learning Objectives

This project helped me explore:

* Integrating an AI model into a Python application.
* Working with APIs and the OpenAI Python SDK.
* Managing environment variables securely.
* Implementing functions and interactive loops.
* Maintaining conversational context using message history.

 If you find this project useful, consider giving the repository a star!
