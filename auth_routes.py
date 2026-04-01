from fastapi import APIRouter,Depends,HTTPException
from models import Usuario
from dependecies import pegar_sessao
from main import bcrypt_context
from schemes import usuarioSchemes, LoginScheme
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["lista"])

def criar_token(id_usuario):
    token = f"asdferdfsegfd{id_usuario}"    
    return token

@auth_router.get("/")
async def home():
    """
    O Usuario so podera acessar esta rota se for autenticado
    """
    return{"Mensagem":" tu acessou a rota de autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_Schemes:usuarioSchemes,session:Session =Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_Schemes.email).first()
    if usuario:
        raise HTTPException(status_code=400,detail="E-mail de usuario ja existente")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_Schemes.senha)
        novo_usuario = Usuario(usuario_Schemes.nome, usuario_Schemes.email,senha_criptografada,usuario_Schemes.ativo,usuario_Schemes.admin)
        session.add(novo_usuario)
        session.commit()
        return{"Mensagem":f"usuario cadastrado com sucesso {usuario_Schemes.email}"}  
    
@auth_router.post("/login")
async def login(LoginScheme: LoginScheme,session:Session = Depends(pegar_sessao)):
    usuario= session.query(Usuario).filter(Usuario.email==LoginScheme.email).first()
    if not usuario:
        raise HTTPException(status_code=400,detail="Usuario nao encontrado" )
    else:
        acess_token = criar_token(usuario.id)
        return{"acess_token":acess_token,
               "token_type":"Bearer"
               }