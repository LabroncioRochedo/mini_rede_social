from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.private_chat_schemas import VerMensagem,MandarMensagem,DeletarMensagem
from services.private_chat_services import ver_mensagens,mandar_mensagem,deletar_mensagem

router = APIRouter(prefix="/private_chat",dependencies=[Depends(checar_token)])

@router.post("/ver")
async def ver(friend_id: VerMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return ver_mensagens(friend_id,user_id,db)

@router.post("/mandar")
async def mandar(conteudo: MandarMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return mandar_mensagem(conteudo,user_id,db)

@router.delete("/deletar")
async def deletar(mensagem_id: DeletarMensagem,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return deletar_mensagem(mensagem_id,user_id,db)
