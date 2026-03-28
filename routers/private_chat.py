from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.private_chat_schemas import VerMensagem,MandarMensagem,DeletarMensagem
from services.private_chat_services import ver_mensagens,mandar_mensagem,deletar_mensagem

router = APIRouter(prefix="/private_chat",dependencies=[Depends(checar_token)])

@router.post("/ver")
def ver(friend_id: VerMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_mensagens(friend_id,user_id,db)

@router.post("/mandar")
def mandar(conteudo: VerMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_mensagens(conteudo,user_id,db)

@router.delete("/deletar")
def deletar(mensagem_id: VerMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_mensagens(mensagem_id,user_id,db)
