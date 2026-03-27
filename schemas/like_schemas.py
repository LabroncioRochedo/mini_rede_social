from pydantic import BaseModel

class EnviarLike(BaseModel):
    comment_id = int