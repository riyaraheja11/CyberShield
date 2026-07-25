from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import ask_gemini

router = APIRouter()

class AnalyzeRequest(BaseModel):
    transcript: str


@router.post("/analyze-call")
async def analyze_call(request: AnalyzeRequest):

    transcript = request.transcript

    prompt = f"""
You are an AI Cyber Fraud Detection Expert.

Analyze the following phone call transcript.

Transcript:
{transcript}

Return:
1. Threat Score (0-100)
2. Risk Level
3. Scam Type
4. Suspicious Keywords
5. Emotional State
6. Explanation
7. Safety Advice
"""

    result = ask_gemini(prompt)

    return {
        "status": "success",
        "transcript": transcript,
        "analysis": result
    }