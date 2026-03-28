from pydantic import BaseModel

class MandarMensagem(BaseModel):
    friend_id: int
    conteudo: str

class DeletarMensagem(BaseModel):
    mensagem_id: int

class VerMensagem(BaseModel):
    friend_id: int