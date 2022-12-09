from typing import Any
from pydantic import BaseModel
from datetime import datetime

class BeneficiaryBase(BaseModel):
    id: int
    name: str
    relationship_to_employee: str
    birthday: datetime
    gender: str  
    employee_id: int
    employee: Any

    class Config:
        orm_mode = True

class BeneficiaryCreate(BaseModel):
    """ Beneficiary Create """
    name: str
    relationship_to_employee: str
    birthday: datetime
    gender: str
    employee_id: int

class BeneficiaryUpdate(BaseModel):
    """ Beneficiary Update """
    name: str
    relationship_to_employee: str
    birthday: datetime
    gender: str
    employee_id: int

class Beneficiary(BeneficiaryBase):
    """ Beneficiary """