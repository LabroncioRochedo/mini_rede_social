from pydantic import BaseModel, Field

class UsuarioCreat(BaseModel):

    nome: str = Field(min_length=4, max_length=22)
    senha: str = Field(min_length=8, max_lenght=40)