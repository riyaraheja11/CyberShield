from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import ask_gemini

router = APIRouter()

class VerifyRequest(BaseModel):
    authority: str

@router.post("/verify-authority")
async def verify_authority(request: VerifyRequest):

    prompt = f"""
You are CyberShield AI.

Verify whether this organization or authority is legitimate.

Authority:
{request.authority}

Return:
1. Legitimate or Suspicious
2. Reason
3. Safety Advice
"""

    result = ask_gemini(prompt)

    return {
        "status": "success",
        "verification": result
    }