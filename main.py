#para rodar o codigo usar o comando: uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv 
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
#*necessario transforma-lo em numero inteiro,para indicar o tempo de expiração do token*#
ACESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("ACESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router) 