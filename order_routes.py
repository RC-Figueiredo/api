from fastapi import APIRouter

order_router= APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Esta rota é dedicada aos pedidos 
    """
    return {"mensagem":" Você acessou a rota pedidos"}
      