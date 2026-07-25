from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import ask_gemini

router = APIRouter()

class ExplainRequest(BaseModel):
    text: str

@router.post("/explain-ai")
async def explain_ai(request: ExplainRequest):

    prompt = f"""
You are CyberShield AI.

Explain the following cyber fraud or scam message in simple language.

Message:
{request.text}

Explain:
1. What is happening?
2. Why is it suspicious?
3. What should the user do?
"""

    result = ask_gemini(prompt)

    return {
        "status": "success",
        "explanation": result
    }