from pydantic import BaseModel

class EnviarLike(BaseModel):
    post_id: int