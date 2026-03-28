from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.friend_request_schemas import EnviarPedido,ResponderPedido
from services.friend_request_services import enviar_pedido,responder_pedido,ver_pedidos_enviados,ver_pedidos_recebidos

router = APIRouter(prefix="/pedidos",dependencies=[Depends(checar_token)])

@router.post("/enviar")
async def enviar(destinatario_id: EnviarPedido,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return enviar_pedido(destinatario_id,user_id,db)

@router.post("/responder")
async def responder(conteudo:ResponderPedido,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return responder_pedido(conteudo,user_id,db)

@router.get("/enviados")
async def ver_enviador(db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_pedidos_enviados(user_id,db)

@router.get("/recebidos")
async def ver_enviador(db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_pedidos_recebidos(user_id,db)