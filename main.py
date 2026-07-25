from fastapi import FastAPI
from app.routers.verify import router as verify_router
from app.routers.analyze import router as analyze_router
from app.routers.emotion import router as emotion_router
from app.routers.contacts import router as contacts_router
from app.routers.livemonitor import router as live_router
from app.routers.panic import router as panic_router
from app.routers.elderly import router as elderly_router
from app.routers.safety import router as safety_router
from app.routers.explain import router as explain_router
from app.routers.chatbot import router as chatbot_router
from app.routers.dashboard import router as dashboard_router
from app.routers.notifications import router as notifications_router

app = FastAPI(
    title="CyberShield API",
    version="1.0.0",
    description="CyberShield Scam Detection Backend"
)

app.include_router(analyze_router)
app.include_router(verify_router)
app.include_router(emotion_router)
app.include_router(contacts_router)
app.include_router(live_router)
app.include_router(panic_router)
app.include_router(elderly_router)
app.include_router(safety_router)
app.include_router(explain_router)
app.include_router(chatbot_router)
app.include_router(dashboard_router)
app.include_router(notifications_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to CyberShield Backend",
        "status": "Running Successfully"
    }