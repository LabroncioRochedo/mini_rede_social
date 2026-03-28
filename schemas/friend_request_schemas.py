from pydantic import BaseModel

class EnviarPedido(BaseModel):
    destinatario_id: int

class ResponderPedido(BaseModel):
    pedido_id: int
    resposta: bool

