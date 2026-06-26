from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, String, Integer
from app.database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=True)
    concluida: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)
