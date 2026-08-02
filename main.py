#* para rodar o porjeto utilize o comando python -m uvicorn main:app --reload *#
from fastapi import FastAPI

app= FastAPI()  

# importar os roteadores de requisições
from auth_routes import auth_router
from order_routes import order_router

# incluir os roteadores a aba main
app.include_router(auth_router)
app.include_router(order_router)