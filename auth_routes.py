from fastapi import APIRouter,Depends,HTTPException
from models import Usuario
from dependecies import pegar_sessao
from main import bcrypt_context
from schemes import usuarioSchemes

auth_router = APIRouter(prefix="/auth", tags=["lista"])

@auth_router.get("/")
async def home():
    """
    O Usuario so podera acessar esta rota se for autenticado
    """
    return{"Mensagem":" tu acessou a rota de autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_Schemes:usuarioSchemes,session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_Schemes.email).first()
    if usuario:
        raise HTTPException(status_code=400,detail="E-mail de usuario ja existente")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_Schemes.senha)
        novo_usuario = Usuario(usuario_Schemes.nome, usuario_Schemes.email,senha_criptografada,usuario_Schemes.ativo,usuario_Schemes.admin)
        session.add(novo_usuario)
        session.commit()
        return{"Mensagem":f"usuario cadastrado com sucesso {usuario_Schemes.email}"}  