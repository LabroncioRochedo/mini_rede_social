from pydantic import BaseModel

class EnviarComentario(BaseModel):
    conteudo: str
    post_id: int

class DeletarComentario(BaseModel):
    post_id: int

class ListarComentarios(BaseModel):
    post_id: int