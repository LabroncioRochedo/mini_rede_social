from models.friend_request_model import FriendRequest
from models.user_model import Usuario
from models.friend_model import Friend
from fastapi import HTTPException

def enviar_pedido(destinatario_id,remetente_id,db):

    verificar_usuario = db.query(Usuario).filter(Usuario.id == destinatario_id.destinatario_id).first()

    if not verificar_usuario:
        HTTPException(status_code=404,detail="usuario nao encontrado")
    
    novo_pedido = FriendRequest(
        remetente_id=remetente_id,
        destinatario_id=destinatario_id.destinatario_id
    )

    db.add(novo_pedido)
    db.commit()

    return {"msg":"pedido enviado"}

def responder_pedido(conteudo,destinatario_id,db):

    pedido = db.query(FriendRequest).filter(FriendRequest.id == conteudo.id,FriendRequest.destinatario_id == destinatario_id).first()

    if not pedido:
        raise HTTPException(status_code=404,detail="pedido nao encontrado")
    
    if conteudo.resposta:

        novo_amigo = Friend(
            user1_id=pedido.remetente_id,
            user2_id=pedido.destinatario_id
        )

        db.add(novo_amigo)
        db.commit()
        db.delete(pedido)
        db.commit()

        return {"msg":"pedido de amizade aceito"}
    
    db.delete(pedido)
    db.commit()

    return {"msg":"pedido recusado"}

def ver_pedidos_enviados(remetente_id,db):

    pedidos = db.query(FriendRequest).filter(FriendRequest.remetente_id == remetente_id).all()

    if not pedidos:
        return {"msg":"nenhum pedido pendente"}
    
    lista_pedidos = []

    for pedido in pedidos:
        lista_pedidos.append(
            {"id": pedido.destinatario_id},
            {"nome": pedido.user.nome}
        )

    return lista_pedidos

def ver_pedidos_recebidos(destinatario_id,db):

    pedidos = db.query(FriendRequest).filter(FriendRequest.remetente_id == destinatario_id).all()

    if not pedidos:
        return {"msg":"nenhum pedido pendente"}
    
    lista_pedidos = []

    for pedido in pedidos:
        lista_pedidos.append(
            {"id": pedido.remetente_id},
            {"nome": pedido.user.nome}
        )

    return lista_pedidos