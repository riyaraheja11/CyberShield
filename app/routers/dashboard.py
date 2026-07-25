from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
async def dashboard():

    return {
        "status": "success",
        "total_calls": 126,
        "high_risk_calls": 18,
        "safe_calls": 108,
        "trusted_contacts": 5,
        "panic_alerts": 2,
        "recent_activity": [
            "Scam call detected",
            "Authority verified",
            "Live monitoring completed"
        ]
    }