from fastapi import APIRouter

router = APIRouter()

@router.get("/psychological-safety")
async def psychological_safety():

    return {
        "stress_level": 72,
        "fear_level": 88,
        "confidence": 35,
        "panic_probability": 82,
        "recommendation": "High emotional manipulation detected. End the call immediately."
    }