# 🏨 Stay O'clock Hotel Chatbot

A smart AI-powered hotel assistant built using **FastAPI**, **LangChain**, and **llama3-8b-8192**. This chatbot helps users inquire about room availability, services, hotel policies, and more — via **WhatsApp** or web-based UI. It handles predefined questions with instant replies and routes unknown queries for manual handling.

---

## 🌐 Live Use Case
**Hotel Name:** Stay O'clock Hotel and Restaurant  
**Location:** Skardu (Clifton Pul near Abdullah Hospital)  
**Email:** stayoclockhotel@gmail.com

---

## 🚀 Features

- ✅ **Instant replies** to common hotel-related queries
- 📦 **Room availability check** with dynamic/manual updates
- 🧠 **LLM-based understanding** of customer questions
- 💬 **WhatsApp-compatible responses** (or extend to Instagram)
- ⛓️ Powered by **LangChain** and **llama3-8b-8192**
- 🗃️ Static and dynamic hotel data support
- ⚙️ Easily extendable and production-ready structure

---

## 📁 Folder Structure

```
hotel_bot/
│
├── app/
│ ├── build_vector_db.py # Script to build FAISS vector DB from hotel info
│ ├── embedder.py # (Optional) Alternate vector builder
│ ├── main.py # FastAPI backend with web UI
│ ├── rag.py # Core RAG logic using LangChain + Groq LLM
│ ├── static_data.txt # Static hotel information (used for embeddings)
│ ├── vectordb.pkl/ # FAISS vector index (generated after running vector builder)
│
├── .env # Contains your OPENROUTER_API_KEY (used for Groq)
├── requirements.txt # Project dependencies
├── README.md # Project documentation (you’re reading it!)
└── venv/ # Virtual environment (optional)
```
---

## 🧠 Tech Stack

- **Backend:** FastAPI
- **LLM:** llama3-8b-8192 via HuggingFace or Groq API
- **Embedding:** Hugging Face Transformers
- **RAG Engine:** LangChain
- **Database:** SQLite (or static file-based for now)

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/hotel-chatbot.git
cd hotel-chatbot

## Create virtual environment

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

## Install Dependencies

pip install -r requirements.txt

## Setup environment variables
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here

## Run the FastAPI server

uvicorn app.main:app --reload
