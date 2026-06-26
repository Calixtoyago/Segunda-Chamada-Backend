from sqlalchemy.exc import SQLAlchemyError
from app.repositories.repositories import *
from app.schemas.schema import TarefasCreate
from app.models.models import Tarefa
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

def criar_tarefa_service(db: Session, tarefa: TarefasCreate):
    nova_tarefa = criar_tarefa_repository(db, tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return {
        "status_code": 201,
        "content": "Tarefa criada!"
    }

def listar_tarefa_service(db: Session, limit: int = 10, offset: int = 0):
    return listar_tarefas_repository(db, limit, offset)
    
        