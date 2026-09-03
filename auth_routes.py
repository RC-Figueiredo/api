from fastapi import APIRouter
from models import Usuario,db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix= "/auth",tags=["Autenticacao"])

@auth_router.get("/")

async def home():
    # para deixar comentario usar 6 aspas
    """
    Esta rota é de autenticacao, somente usuarios autorizados conseguem o acesso
    """

    return{"Mensagem":"Autenticado com sucesso","Autenticado":False}

@auth_router.post("/criar_usuario")
async def criar_conta(email:str,senha:str, nome:str,telefone:int,endereco:str):
    # criando conexão com o banco de dados
    Session = sessionmaker(bind=db)
    # criação da sessao para executar tal sessão,a session permitirá com que o banco de dados na+ão fique com requisições em aberto e faça outra busca em simultaneo
    session=Session()
    usuario = session.query(Usuario).filter(Usuario.email== email).first()

    if usuario:
        return{"Mensagem":"Existe um usuario ja com este email"}
    else:
        novo_usuario = Usuario(nome,email,senha,telefone,endereco)
        session.add(novo_usuario)
        session.commit()
        return{"Mensagem":"usuario cadastrado com sucesso"}