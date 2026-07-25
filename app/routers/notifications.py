from fastapi import APIRouter

router = APIRouter()

@router.get("/notifications")
async def notifications():

    return {
        "status": "success",
        "notifications": [
            {
                "title": "Scam Alert",
                "message": "A high-risk scam call was detected."
            },
            {
                "title": "Safety Tip",
                "message": "Never share OTP or banking credentials."
            }
        ]
    }