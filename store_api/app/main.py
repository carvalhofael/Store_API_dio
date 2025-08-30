from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Store API")

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "API rodando!"}