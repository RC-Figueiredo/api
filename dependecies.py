from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    #* "try" tenta executar o codigo,yield returna o valor mas nao encerra o codigo,finally finaliza e fecha o session independente do que aconteça*#
    try:
        Session= sessionmaker(bind=db)
        session = Session()    
        yield session
    finally:
        session.close()