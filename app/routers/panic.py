from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PanicRequest(BaseModel):
    latitude: float
    longitude: float

@router.post("/panic")
async def panic_mode(data: PanicRequest):
    return {
        "status": "Emergency Triggered",
        "location": {
            "latitude": data.latitude,
            "longitude": data.longitude
        },
        "contacts_notified": True,
        "police_alert": False,
        "message": "Emergency alert sent to trusted contacts."
    }