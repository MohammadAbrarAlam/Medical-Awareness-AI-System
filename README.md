# 🩺 Medical Awareness AI System (CrewAI + Gemini + Flask)

An AI-powered Medical Awareness System that analyzes diseases, symptoms, causes, and prevention methods using CrewAI multi-agent workflow and Google Gemini LLM. It generates structured, easy-to-understand medical awareness reports through a Flask REST API.

---

## 🚀 Features

- 🧠 Multi-Agent AI system using CrewAI
- 🔍 Real-time web search using Serper API
- 🤖 Google Gemini 2.5 Flash integration
- 📘 Converts complex medical data into simple language
- 🛡 Provides disease prevention and health tips
- 🔬 Fact-checking and validation workflow
- 🌐 REST API built with Flask
- ☁️ Ready for deployment on Render

---

## 🏗 Tech Stack

- Python 🐍
- Flask 🌐
- CrewAI 🤖
- Google Gemini API ✨
- Serper API 🔍
- python-dotenv 🔐

---

## 📁 Project Structure

medical_awareness/
│── app.py
│── crews.py
│── agents.py
│── tasks.py
│── requirements.txt
│── runtime.txt
│── render.yaml
│── .gitignore
│── README.md

---

## ⚙️ Installation

### 1. Clone repository
git clone https://github.com/your-username/medical-awareness-ai.git
cd medical-awareness-ai

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

---

## 🔐 Environment Variables

Create a `.env` file in root directory:

GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key

---

## ▶️ Run Locally

python app.py

Server will run at:
http://localhost:5000

---

## 📡 API Usage

### Endpoint
POST /analyze

### Request Body
{
  "topic": "diabetes"
}

### Response Example
{
  "success": true,
  "topic": "diabetes",
  "result": "AI generated structured medical awareness report..."
}

---

## ☁️ Deploy on Render

Steps:
1. Push project to GitHub
2. Connect repo on Render
3. Add environment variables:
   - GEMINI_API_KEY
   - SERPER_API_KEY
4. Deploy using render.yaml

---

## 🧠 Agent Architecture

- Research Agent → Collects medical data from web
- Simplifier Agent → Converts complex info into simple language
- Prevention Agent → Provides health & lifestyle tips
- Fact Checker Agent → Validates medical accuracy
- Response Agent → Generates final structured report

---

## ⚠️ Disclaimer

This project is for educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.

---

## 👨‍💻 Author

Developed by: Abrar Alam

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.
