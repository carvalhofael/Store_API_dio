from fastapi import APIRouter

router = APIRouter()

# Exemplo de rota
@router.get("/")
async def home():
    return {"message": "Bem-vindo à Store API!"}