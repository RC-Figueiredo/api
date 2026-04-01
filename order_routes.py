from fastapi import APIRouter, Depends
from schemes import pedidoSchemes
from dependecies import pegar_sessao
from models import Pedido
from sqlalchemy.orm import Session

order_router= APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Esta rota é dedicada aos pedidos 
    """
    return {"mensagem":" Você acessou a rota pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_Schemes:pedidoSchemes,session :Session= Depends(pegar_sessao)):

    novo_pedido = Pedido(usuario = pedido_Schemes.usuario)
    session.add(novo_pedido)
    session.commit()
    return{"Mensagem":f"pedido criado com sucesso {novo_pedido.id}"}