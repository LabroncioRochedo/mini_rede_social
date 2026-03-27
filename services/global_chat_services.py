from models.global_chat_model import GlobalChat
from fastapi import HTTPException

def criar_post(conteudo,user_id,db):

    novo_post = GlobalChat(
        user_id = user_id,
        conteudo = conteudo.conteudo
    )
    db.add(novo_post)
    db.commit()
    return {"msg":"post criado"}

def listar_posts(db,user_id):
    posts = db.query(GlobalChat).all()
    resultado = []

    for post in posts:
        curtido_por_mim = any(like.user_id == user_id for like in post.like)

        resultado.append({
            "id": post.id,
            "conteudo": post.conteudo,
            "usuario_id": post.user_id,
            "likes": len(post.like),
            "comentarios": len(post.comment),
            "data_de_envio": post.data_de_envio,
            "curtido_por_mim": curtido_por_mim
        })
    
    return resultado


def deletar_post(post_id,user_id,db):
    post = db.query(GlobalChat).filter(GlobalChat.user_id == user_id, GlobalChat.id == post_id.post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="post nao encontrado")
    db.delete(post)
    db.commit()
    return {"msg":"post deletado"}
