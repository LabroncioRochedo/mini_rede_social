from models.global_chat_model import GlobalChat
from fastapi import HTTPException

def criar_post(conteudo,user_id,db):

    novo_post = GlobalChat(
        user_id = user_id,
        conteudo = conteudo.conteudo,
        likes = 0,
        comments = 0
    )
    db.add(novo_post)
    db.commit()
    return {"msg":"post criado"}

def listar_posts(db):
    posts = db.query(GlobalChat).all()
    return posts

def deletar_post(post_id,user_id,db):
    post = db.query(GlobalChat).filter(GlobalChat.user_id == user_id, GlobalChat.id == post_id.post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="post nao encontrado")
    db.delete(post)
    db.commit()
    return {"msg":"post deletado"}
