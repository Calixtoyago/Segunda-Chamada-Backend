from fastapi import FastAPI, 
from app.routers.router import router as tarefas_router




app = FastAPI(
    title="API - Segunda Chamada",
    description="API para gerenciar tarefas",
    version="1.0.0"
)

app.include_router(tarefas_router)

@app.get("/")
def health_check():
    return {
        "status": "online",
        "mensagem": "A API está rodando"
    }