from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from security.tokens import checar_token
from schemas.global_chat_schemas import GlobalChatCreat,GlobalChatDelete
from services.global_chat_services import criar_post,listar_posts,deletar_post

router = APIRouter(prefix="/global_chat",dependencies=[Depends(checar_token)])

@router.post("/")
async def criar(conteudo: GlobalChatCreat,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return criar_post(conteudo,user_id,db)

@router.get("/")
async def listar(db: Session = Depends(get_db)):
    return listar_posts(db)

@router.delete("/")
async def deletar(post_id: GlobalChatDelete,db: Session = Depends(get_db),user_id: int = Depends(checar_token)):
    return deletar_post(post_id,user_id,db)