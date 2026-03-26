from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["lista"])

@auth_router.get("/")
async def home():
    """
    O Usuario so podera acessar esta rota se for autenticado
    """
    return{"Mensagem":" tu acessou a rota de autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str,senha: str,nome: str):
    Session= sessionmaker(bind=db)
    session=Session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return{"Mensagem":"ja existe um usuario com exste email"}
    else:
        novo_usuario = Usuario(nome, email,senha)
        session.add(novo_usuario)
        session.commit()
        return{"Mensagem":"usuario cadastrado com sucesso"}