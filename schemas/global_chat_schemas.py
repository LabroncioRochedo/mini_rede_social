from pydantic import BaseModel,Field

class GlobalChatCreat(BaseModel):
    conteudo: str = Field(min_length=1, max_length=1000)

class GlobalChatDelete(BaseModel):
    post_id = int