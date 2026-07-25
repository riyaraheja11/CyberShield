from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import ask_gemini

router = APIRouter()

class EmotionRequest(BaseModel):
    transcript: str

@router.post("/emotion-analysis")
async def emotion_analysis(request: EmotionRequest):

    prompt = f"""
You are an AI emotion detection expert.

Analyze the following conversation.

Conversation:
{request.transcript}

Return:
1. Fear Level
2. Urgency
3. Stress
4. Confidence
5. Explanation
"""

    result = ask_gemini(prompt)

    return {
        "status": "success",
        "emotion": result
    }