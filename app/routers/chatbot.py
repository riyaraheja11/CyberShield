from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import ask_gemini

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chatbot")
async def chatbot(request: ChatRequest):

    prompt = f"""
You are CyberShield AI.

You are an expert cyber security assistant.

User Question:
{request.message}

Give a short, clear and practical answer.
"""

    response = ask_gemini(prompt)

    return {
        "status": "success",
        "reply": response
    }