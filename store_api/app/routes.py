from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Bem-vindo à Store API!"}
