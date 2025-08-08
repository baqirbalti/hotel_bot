# 🏨 Stay O'clock Hotel Chatbot

A smart AI-powered hotel assistant built using **FastAPI**, **LangChain**, and **Mistral LLM**. This chatbot helps users inquire about room availability, services, hotel policies, and more — via **WhatsApp** or web-based UI. It handles predefined questions with instant replies and routes unknown queries for manual handling.

---

## 🌐 Live Use Case
**Hotel Name:** Stay O'clock Hotel and Restaurant  
**Location:** Skardu (Clifton Pul near Abdullah Hospital)  
**Email:** baqirbalti777@gmail.com

---

## 🚀 Features

- ✅ **Instant replies** to common hotel-related queries
- 📦 **Room availability check** with dynamic/manual updates
- 🧠 **LLM-based understanding** of customer questions
- 💬 **WhatsApp-compatible responses** (or extend to Instagram)
- ⛓️ Powered by **LangChain** and **Mistral-7B-Instruct**
- 🗃️ Static and dynamic hotel data support
- ⚙️ Easily extendable and production-ready structure

---

## 📁 Folder Structure

```
hotel-chatbot/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── models/ # Data models (Room, Booking)
│ ├── database/ # SQLite DB setup (or mock for static)
│ ├── rag/ # RAG logic using LangChain
│ └── utils/ # Helper functions
│
├── data/
│ └── hotel_info.txt # Static hotel info for embedding
│
├── vectordb/
│ └── vectordb.pkl # Vector DB with embeddings
│
├── .env # Environment variables (e.g., Groq API key)
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

```
---

## 🧠 Tech Stack

- **Backend:** FastAPI
- **LLM:** Mistral 7B via HuggingFace or Groq API
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
