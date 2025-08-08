from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

def build_vector_db():
    loader = TextLoader("app/static_data.txt")  # load the hotel info
    documents = loader.load()

    # Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS vector DB
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local("app/vectordb.pkl")
    print("✅ Vector DB saved to app/vectordb.pkl")

if __name__ == "__main__":
    build_vector_db()
