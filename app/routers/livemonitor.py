from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()

class LiveTranscript(BaseModel):
    transcript: str

@router.post("/live-monitor")
async def live_monitor(data: LiveTranscript):

    score = random.randint(20, 98)

    if score >= 80:
        level = "HIGH"
    elif score >= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "transcript": data.transcript,
        "threat_score": score,
        "risk_level": level,
        "alert": score >= 80
    }