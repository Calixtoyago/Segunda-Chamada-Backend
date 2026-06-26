from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.models.models import Tarefa


def criar_tarefa_repository(db: Session, tarefa):
    novo_user = Tarefa(
        titulo = tarefa.titulo,
        descricao = tarefa.descricao,
    )
    db.add(novo_user)
    db.flush()
    return novo_user

def listar_tarefas_repository(db: Session, limit: int, offset: int):
    query = select(Tarefa).limit(limit).offset(offset)
    return db.execute(query).scalars().all()

def atualizar_tarefa_repository(db: Session, id: int):
    stmt = (
        update(Tarefa)
        .values(concluida=True)
    )
    return db.execute(stmt)

def deletar_tarefa_repository(db: Session, id: int):
    query = select(Tarefa).where(Tarefa.id==id).scalar_one_or_none()
    return db.delete(query)