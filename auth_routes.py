from fastapi import APIRouter,Depends,HTTPException
from models import Usuario
from dependecies import pegar_sessao,verificar_token
from main import bcrypt_context, ALGORITHM, ACESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY
from schemes import usuarioSchemes, LoginScheme
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone 
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix="/auth", tags=["lista"])
#*cria o token de autenticação e cronomeetra o tempo de expiração*#
def criar_token(id_usuario,duracao_token = timedelta(minutes = ACESS_TOKEN_EXPIRE_MINUTES)):#*cria o hash,que seria a criptografia da senha*#
    #JWT
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub":str(id_usuario),"exp":data_expiracao }
    jwt_codificado = jwt.encode(dic_info,SECRET_KEY,ALGORITHM ) 

    return jwt_codificado
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#
def autenticar_usuario(email,senha,session):
    usuario= session.query(Usuario).filter(Usuario.email==email).first()#*irá verificar se a hash e a senha utilizada por um usuario especifico,coonfere,se é permitido liberar o acesso*#
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha,usuario.senha):
        return False
    return usuario
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#

@auth_router.get("/")
async def home():
    """
    O Usuario so podera acessar esta rota se for autenticado
    """
    return{"Mensagem":" tu acessou a rota de autenticação"}

@auth_router.post("/criar_conta")
#*função de criar a conta do usuario,se caso não existente*#
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

#*verifica se o usuario existe e se ele esta com o acesso permitido para fazer o login  *#
@auth_router.post("/login")
async def login(LoginScheme: LoginScheme,session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(LoginScheme.email, LoginScheme.senha, session)

    if not usuario:
        raise HTTPException(status_code=400,detail="Usuario nao encontrado ou credenciais incorretas" )
    else:
        acess_token = criar_token(usuario.id)
        refresh_token=criar_token(usuario.id,duracao_token=timedelta(days=7) )
        return{"acess_token":acess_token,
               "refresh_token":refresh_token,
               "token_type":"Bearer"
               }
#*segundo login*#
@auth_router.post("/login-form")
async def login_form(dados_formulario: OAuth2PasswordRequestForm= Depends(),session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(dados_formulario.username,dados_formulario.password, session)

    if not usuario:
        raise HTTPException(status_code=400,detail="Usuario nao encontrado ou credenciais incorretas" )
    else:
        acess_token = criar_token(usuario.id)
        return{"acess_token":acess_token,
               "token_type":"Bearer"
               }

    
@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario= Depends(verificar_token)):
    #*verificação do token*#
   acess_token= criar_token(usuario.id)
   return{
    "acess_token": acess_token,
    "token_type":"Bearer"
               }
