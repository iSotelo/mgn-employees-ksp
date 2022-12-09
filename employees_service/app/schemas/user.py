from typing import Any, Union
from pydantic import BaseModel
from pydantic.schema import Optional

class UsuarioBase(BaseModel):
    """ Usuario Base """
    id: int
    nombre:str
    username: str
    password: str

    class Config:
        orm_mode = True

class UsuarioCreate(BaseModel):
    """ Usuario Create """
    nombre:str
    username: str
    password: str

class UsuarioUpdate(BaseModel):
    """ Usuario Update """
    nombre:str
    username: str
    password: str

class Usuario(UsuarioBase):
    """ Usuario """