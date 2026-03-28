from pydantic import BaseModel,Field

class EnviarComentario(BaseModel):
    conteudo: str = Field(min_length=1, max_length=1000)
    post_id: int

class DeletarComentario(BaseModel):
    comment_id: int

class ListarComentarios(BaseModel):
    post_id: int