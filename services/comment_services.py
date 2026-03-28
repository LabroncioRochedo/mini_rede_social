from models.comment_model import Comment
from models.global_chat_model import GlobalChat
from fastapi import HTTPException

def enviar_comentario(conteudo,user_id,db):
    verificar_post = db.query(GlobalChat).filter(GlobalChat.id == conteudo.post_id).first()

    if not verificar_post:
        raise HTTPException(status_code=404,detail="post nao encontrado")
    
    novo_comentario = Comment(
        global_chat_id=conteudo.post_id,
        user_id=user_id,
        conteudo=conteudo.conteudo
    )

    db.add(novo_comentario)
    db.commit()
    return {"msg":"comentario feito"}

def listar_comentarios(post_id,db):
    verificar_post = db.query(GlobalChat).filter(GlobalChat.id == post_id.post_id).first()

    if not verificar_post:
        raise HTTPException(status_code=404,detail="post nao encontrado")
    
    comentarios = db.query(Comment).filter(Comment.global_chat_id == post_id.post_id).all()

    if not comentarios:
        return {"msg":"sem comentarios no momento"}
    
    return comentarios

def deletar_comentario(comment_id,user_id,db):
    comentario = db.query(Comment).filter(Comment.id == comment_id.comment_id, Comment.user_id == user_id).first()

    if not comentario:
        raise HTTPException(status_code=404,detail="comentario nao encontrado")
    
    db.delete(comentario)
    db.commit()
    return {"msg":"comentairo deletado"}
