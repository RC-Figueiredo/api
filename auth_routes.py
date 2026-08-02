from fastapi import APIRouter

auth_router = APIRouter(prefix= "/auth",tags=["Autenticacao"])

@auth_router.get("/")

async def login():
    # para deixar comentario usar 6 aspas
    """
    Esta rota é de autenticacao, somente usuarios autorizados conseguem o acesso
    """

    return{"Mensagem":"Autenticado com sucesso","Autenticado":False}