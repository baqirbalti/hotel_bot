from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.rag import get_bot

app = FastAPI()
qa_chain = get_bot()

class UserQuery(BaseModel):
    question: str

# Simple HTML template for web interface
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Stay O'Clock Hotel Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .chat-container { border: 1px solid #ccc; padding: 20px; border-radius: 10px; margin: 20px 0; }
        .input-container { display: flex; gap: 10px; margin: 20px 0; }
        input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .response { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; }
        .loading { color: #666; font-style: italic; }
    </style>
</head>
<body>
    <h1>🏨 Stay O'Clock Hotel Chatbot</h1>
    <div class="chat-container">
        <div class="input-container">
            <input type="text" id="question" placeholder="Ask about our hotel..." onkeypress="if(event.key=='Enter') askQuestion()">
            <button onclick="askQuestion()">Ask</button>
        </div>
        <div id="response"></div>
    </div>

    <script>
        async function askQuestion() {
            const question = document.getElementById('question').value;
            if (!question) return;
            
            const responseDiv = document.getElementById('response');
            responseDiv.innerHTML = '<div class="loading">Thinking...</div>';
            
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: question })
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                responseDiv.innerHTML = '<div class="response"><strong>Answer:</strong><br>' + data.answer + '</div>';
            } catch (error) {
                responseDiv.innerHTML = '<div class="response" style="color: red;">Error: ' + error.message + '</div>';
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return html_content

@app.post("/ask")
def ask_bot(query: UserQuery):
    try:
        answer = qa_chain.invoke({"query": query.question})
        return {"answer": answer["result"]}
    except Exception as e:
        return {"answer": f"Sorry, I encountered an error: {str(e)}"}
