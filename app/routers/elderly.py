from fastapi import APIRouter

router = APIRouter()

@router.get("/elderly-mode")
async def elderly_mode():
    return {
        "large_text": True,
        "voice_assistance": True,
        "high_contrast": True,
        "emergency_button": True,
        "status": "Enabled"
    }