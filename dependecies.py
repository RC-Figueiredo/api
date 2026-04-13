from fastapi import Depends
from models import db
from sqlalchemy.orm import sessionmaker,Session
from models import Usuario


def pegar_sessao():
    #* "try" tenta executar o codigo,yield returna o valor mas nao encerra o codigo,finally finaliza e fecha o session independente do que aconteça*#
    try:
        Session= sessionmaker(bind=db)
        session = Session()    
        yield session
    finally:
        session.close()
        
#*---------------------------------------------------------------------------------------------------------------------------------------------------------*#
def verificar_token(token,session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.id==1).first()

    return usuario