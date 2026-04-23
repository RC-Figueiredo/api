from fastapi import APIRouter, Depends, HTTPException
from schemes import pedidoSchemes
from dependecies import pegar_sessao,verificar_token
from models import Pedido
from sqlalchemy.orm import Session

order_router= APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#
@order_router.get("/")
async def pedidos():
    """
    Esta rota é dedicada aos pedidos 
    """
    return {"mensagem":" Você acessou a rota pedidos"}
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#
@order_router.post("/pedido")
async def criar_pedido(pedido_Schemes:pedidoSchemes,session :Session= Depends(pegar_sessao)):

    novo_pedido = Pedido(usuario = pedido_Schemes.usuario)
    session.add(novo_pedido)
    session.commit()
    return{"Mensagem":f"pedido criado com sucesso {novo_pedido.id}"}
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#
@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session :Session= Depends(pegar_sessao)):
    pedido=session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not Pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")