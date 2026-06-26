from fastapi import APIRouter
from app.schema import TarefasCreate, TarefasResponse
import os
from dotenv import load_dotenv 
from fastapi.responses import JSONResponse

load_dotenv()
titulo = os.getenv("APP_TITLE")

router = APIRouter(tags=["Tarefas"])

tarefas_list = []

#GET - retorna titulo
@router.get("/")
def retornar_titulo():
    return titulo

@router.get("/tarefas")
# def listar_tarefas(response_model=list[TarefasResponse]):
def listar_tarefas():
    global tarefas_list
    return tarefas_list

@router.post("/tarefas", response_model=TarefasResponse)
def criar_tarefa(tarefa: TarefasCreate):
    global tarefas_list

    tarefa_nova = dict(tarefa)

    if len(tarefas_list) == 0:
        id = 0
    else:
        id = tarefas_list[-1]["id"]   

    tarefa_nova["id"] = id + 1
    tarefa_nova["concluida"] = False

    tarefas_list.append(tarefa_nova)

    return JSONResponse(
        status_code=201,
        content="Tarefa criada!"
    )

@router.put("/tarefas/{id}")
def concluir_tarefa(id: int):
    global tarefas_list

    for tarefa in tarefas_list:
        if tarefa["id"] == id:
            tarefa["concluida"] = True
            return JSONResponse(
                content="Tarefa atualizada!"
            )

    return JSONResponse(
        status_code=404,
        content={
            "error": "TAREFA_NAO_ENCONTRADA",
            "message": f"Tarefa com id {id} não foi encontrada"
        },
    )
    
@router.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    global tarefas_list

    for tarefa in tarefas_list:
        if tarefa["id"] == id:
            tarefas_list.remove(tarefa)
            return JSONResponse(
                status_code=204,
                content="Tarefa deletada!"
            )

    return JSONResponse(
        status_code=404,
        content={
            "error": "TAREFA_NAO_ENCONTRADA",
            "message": f"Tarefa com id {id} não foi encontrada"
        },
    )


    