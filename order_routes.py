from fastapi import APIRouter, Depends, HTTPException
from schemes import pedidoSchemes,item_pedido_schema
from dependecies import pegar_sessao,verificar_token
from models import Pedido,Usuario, ItenPedido
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
async def cancelar_pedido(id_pedido: int, session :Session= Depends(pegar_sessao),usuario:Usuario = Depends(verificar_token)):
    pedido=session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not Pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401,detail="Voce nao tem a permissao para mecher neste pedido")
    pedido.status = "CANCELADO"
    session.commit()
    return{
        "Mensagem": f"Pedido numero: {id_pedido} cancelado com sucesso",
        "pedido": pedido
    }

@order_router.get("/Listar")
async def listar_pedidos(session :Session= Depends(pegar_sessao),usuario:Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401,detail="Voce nao possui autorizacao para verificar este pedido")
    else:
        pedidos = session.query(Pedido).all()
        return{
            "pedidos": pedidos
        }

@order_router.post("/pedido/adicionar-item/{id_pedido}")
async def adicionar_item_pedido(id_pedido:int, item_pedido_schema: item_pedido_schema, session:Session = Depends(pegar_sessao), usuario:Usuario= Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido nao existente")
    
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401,detail="Voce nao tem autorizacao para esta operacao")

    item_pedido = ItenPedido (id = id_pedido,quantidade = item_pedido_schema.quantidade,sabor = item_pedido_schema.sabor,tamanho = item_pedido_schema.tamanho,preco_unitario = item_pedido_schema.preco_unitario,pedido = id_pedido)
    pedido.calcular_preco()
    session.add(item_pedido)
    session.commit()

    return{
        "mensagem":"Item criado com sucesso",
        "item_Id":item_pedido.id,
        "preco_unitario":pedido.preco
    }
