from pydantic import BaseModel,Field

class MandarMensagem(BaseModel):
    friend_id: int
    conteudo: str = Field(min_length=1, max_length=1000)

class DeletarMensagem(BaseModel):
    mensagem_id: int

class VerMensagem(BaseModel):
    friend_id: int