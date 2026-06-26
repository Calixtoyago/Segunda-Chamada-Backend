from fastapi import APIRouter, Depends
from app.schemas.schema import TarefasCreate, TarefasResponse
from app.services.services import *
import os
from dotenv import load_dotenv  
from random import randint
from fastapi.responses import JSONResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schema import TarefasCreate, TarefasResponse

load_dotenv()

router = APIRouter(tags=["Tarefas"])

#GET - retorna titulo
titulo = os.getenv("APP_TITLE")
@router.get("/")
def retornar_titulo(db: Session = Depends(get_db)):
    return titulo

@router.get("/tarefas", response_model=list[TarefasResponse])
def listar_tarefas(limit: int, offset: int, db: Session = Depends(get_db)):
    return listar_tarefa_service(db, limit, offset)

@router.post("/tarefas", response_model=TarefasResponse)
def criar_tarefa(tarefa: TarefasCreate, db: Session = Depends(get_db)):
    return criar_tarefa_service(db, tarefa)

# @router.put("/tarefas/{id}")
# def concluir_tarefa(id: int, db: Session = Depends(get_db)):
#     global tarefas_list

#     for tarefa in tarefas_list:
#         if tarefa["id"] == id:
#             tarefa["concluida"] = True
#             return JSONResponse(
#                 content="Tarefa atualizada!"
#             )

#     return JSONResponse(
#         status_code=404,
#         content={
#             "error": "TAREFA_NAO_ENCONTRADA",
#             "message": f"Tarefa com id {id} não foi encontrada"
#         },
#     )
    
# @router.delete("/tarefas/{id}")
# def deletar_tarefa(id: int, db: Session = Depends(get_db)):
#     global tarefas_list

#     for tarefa in tarefas_list:
#         if tarefa["id"] == id:
#             tarefas_list.remove(tarefa)
#             return JSONResponse(
#                 status_code=204,
#                 content="Tarefa deletada!"
#             )

#     return JSONResponse(
#         status_code=404,
#         content={
#             "error": "TAREFA_NAO_ENCONTRADA",
#             "message": f"Tarefa com id {id} não foi encontrada"
#         },
#     )


    