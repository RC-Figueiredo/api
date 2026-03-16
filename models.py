from sqlalchemy  import create_engine, Column,Integer, String,Boolean,Float,ForeignKey 
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#conexao com o banco de dados
db= create_engine("sqlite:///banco.db")

#base do banco de dados
Base = declarative_base()

#classes e tabelas


#usuario
class Usuario(Base):
    __tablename__ =  "usuarios"
    #oq aparece no banco de dados,a criação das colunas
    id = Column("id",Integer,primary_key=True,autoincrement=True, nullable=False)
    nome = Column ("nome",String)
    email =Column ("email",String,nullable=False)
    senha =Column ("senha",String)
    ativo = Column ("ativo",Boolean)
    admin = Column ("admin",Boolean,default=False)
    
    #a execução das colunas do banco,executa linha a linha
    def __init__(self,nome,email,senha,ativo,admin): 
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo 
        self.admin = admin

#pedido

class Pedido(Base):
    __tablename___ = "pedidos"

#choiceType organiza a coluna status,permitindo ter apenas tres opções de valores,construcao do choiceType
    STATUS_PEDIDOS = (
        #*(chave,valor)*#
        ("PENDENTE","PENDENTE")
        ("CANCELADO","CANCELADO")
        ("FINALIZADO","FINALIZADO")
    )

    id = Column("id",Integer,primary_key=True,autoincrement=True,nullable=False)
    status = Column("status",ChoiceType(choices=STATUS_PEDIDOS))#*status pendente,cancelado,finalizado*#
    usuario =Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco",float)
    #item = ("item")

    def __init__(self,id,usuario,status="Pendente",preco=0):
        self.id = id
        self.status = status
        self.usuario = usuario
        self.preco = preco
        #self.item=item

#itens_Pedidos
class ItenPedido(Base):
    __tablename__ = "itenpedidos"

    id = 
    quantidade =
    sabor =
    tamanho = 
    preco_unitario = 
    pedido = 

 