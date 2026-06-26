from pydantic import BaseModel, ConfigDict, field_validator
from fastapi.responses import JSONResponse

class TarefasCreate(BaseModel):
    titulo: str
    descricao: str

    @field_validator("titulo")
    @classmethod
    def titulo_vazio(cls, titulo):
        if len(titulo) == 0 or len(titulo) > 100:
            return JSONResponse(
                status_code=422,
                content={
                    "error": "TITULO_INVALIDO",
                    "message": "O título deve conter entre 1 a 100 caracteres"
                },
            )
        return titulo
    
class TarefasResponse(TarefasCreate):
    id: int
    concluida: bool

    model_config = ConfigDict(from_attributes=True)