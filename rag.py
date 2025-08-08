from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

def get_bot():
    # Check if API key is available
    api_key = os.getenv("OPENROUTER_API_KEY")  # We'll use the same key for Groq
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please check your .env file.")
    
    print("Loaded Groq API Key:", api_key[:10] + "..." + api_key[-10:])  # Show partial key for security
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Check if vector database exists
    if not os.path.exists("app/vectordb.pkl"):
        raise FileNotFoundError("Vector database not found. Please run build_vector_db.py first to create it.")
    
    vectordb = FAISS.load_local("app/vectordb.pkl", embeddings, allow_dangerous_deserialization=True)

    retriever = vectordb.as_retriever(search_type="similarity", k=2)

    # Use a currently supported Groq model
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192",
        temperature=0.7,
        max_tokens=500
    )

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain