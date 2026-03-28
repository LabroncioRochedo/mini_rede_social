from pydantic import BaseModel,Field

class AcharUsuario(BaseModel):
    nome: str = Field(min_length=4, max_length=22)

class VerPostDoUsuario(BaseModel):
    user_id: int