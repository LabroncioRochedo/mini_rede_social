from models.private_chat_model import PrivateChat
from models.friend_model import Friend
from sqlalchemy import or_,and_
from fastapi import HTTPException

def verificar_amizade(friend_id,user_id,db):

    amizade = db.query(Friend).filter(or_(and_(Friend.user1_id == friend_id,Friend.user2_id == user_id),and_(Friend.user2_id == friend_id,Friend.user1_id == user_id))).first()
    
    return amizade

def mandar_mensagem(conteudo,user_id,db):

    resposta = verificar_amizade(conteudo.friend_id,user_id,db)

    if not resposta:

        raise HTTPException(status_code=403,detail="vcs nao sao amigos")

    novo_comentario = PrivateChat(
        remetente_id=user_id,
        destinatario_id=conteudo.friend_id,
        conteudo=conteudo.conteudo
    )

    db.add(novo_comentario)
    db.commit()

def ver_mensagens(friend_id,user_id,db):

    resposta = verificar_amizade(friend_id.friend_id,user_id,db)

    if not resposta:

        raise HTTPException(status_code=403,detail="vcs nao sao amigos")
    
    mensagens = db.query(PrivateChat).filter(or_(and_(PrivateChat.remetente_id == friend_id.friend_id,PrivateChat.destinatario_id == user_id),and_(PrivateChat.destinatario_id == friend_id.friend_id,PrivateChat.remetente_id == user_id))).all()
    
    lista_mensagens = []

    for mensagem in mensagens:

        lista_mensagens.append(
            {"id": mensagem.id},
            {"remetente": mensagem.remetente.nome},
            {"destinatario":mensagem.destinatario.nome},
            {"data_de_envio": mensagem.data_de_envio}
        )

    return lista_mensagens

def deletar_mensagem(mensagem_id,user_id,db):

    mensagem = db.query(PrivateChat).filter(PrivateChat.id == mensagem_id.mensagem_id, PrivateChat.remetente_id == user_id).first()

    if not mensagem:
        HTTPException(status_code=404,detail="mensagem nao encontrada")
    
    db.delete(mensagem)
    db.commit()

    return {"msg":"mensagem apagada"}
