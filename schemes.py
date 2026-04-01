from pydantic import BaseModel
from typing import Optional

class usuarioSchemes(BaseModel):
    nome:str
    email:str
    senha:str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes= True

class pedidoSchemes(BaseModel):
    usuario: int

    class Config:
        from_attributes = True

class LoginScheme(BaseModel):
    email:str
    senha:str

    class Config:
        from_attributes =True