from pydantic import BaseModel

class AcharUsuario(BaseModel):
    nome: str

class VerPostDoUsuario(BaseModel):
    user_id = int