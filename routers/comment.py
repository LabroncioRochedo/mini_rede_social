from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.comment_schemas import EnviarComentario,DeletarComentario
from services.comment_services import enviar_comentario,deletar_comentario

router = APIRouter(prefix="/comment",dependencies=[Depends(checar_token)])

@router.post("/")
async def enviar(conteudo: EnviarComentario,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return enviar_comentario(conteudo,user_id,db)

@router.delete("/")
async def deletar(comment_id: DeletarComentario,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return deletar_comentario(comment_id,user_id,db)