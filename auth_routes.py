from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["lista"])

@auth_router.get("/")
async def autenticar():
    """
    O Usuario so podera acessar esta rota se for autenticado
    """
    return{"Mensagem":" tu acessou a rota de autenticação"}