from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Contact(BaseModel):
    name: str
    phone: str

trusted_contacts = []

@router.get("/trusted-contacts")
async def get_contacts():
    return trusted_contacts

@router.post("/trusted-contacts")
async def add_contact(contact: Contact):
    trusted_contacts.append(contact)
    return {
        "status": "success",
        "message": "Trusted contact added",
        "contact": contact
    }