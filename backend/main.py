from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mistral model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=150
)

# Conversation history
message = [
    SystemMessage(
        content="""You are a healthcare smart assistant.

Your job is to provide clear, concise, and helpful health information.

Rules:
- Keep responses short and easy to understand.
- Usually respond in 2-4 sentences.
- Give practical, general health guidance.
- Do not diagnose diseases with certainty.
- Do not claim to replace a doctor.
- If symptoms could indicate an emergency, clearly recommend seeking urgent medical care.
- Ask a brief follow-up question when important information is missing.
- Avoid unnecessary medical jargon.
- Do not use excessive headings or formatting.
"""
    )
]


# Request format
class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    # Add user's message
    message.append(
        HumanMessage(content=request.message)
    )

    # Get AI response
    response = model.invoke(message)

    # Store AI response in conversation history
    message.append(response)

    return {
        "response": response.content
    }