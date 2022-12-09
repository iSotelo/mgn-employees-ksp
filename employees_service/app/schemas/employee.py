from typing import Any, Optional
from pydantic import BaseModel
from datetime import datetime

class EmployeeBase(BaseModel):
    id: int
    name: str
    worker_position: str
    salary: float
    status: bool
    hire_date: datetime
    beneficiaries: list[Any]
    
    class Config:
        orm_mode = True
        
class EmployeeCreate(BaseModel):
    """ Employee Create """
    name: str
    worker_position: str
    salary: float
    status: bool
    hire_date: datetime

class EmployeeUpdate(BaseModel):
    """ Employee Update """
    name: str
    worker_position: str
    salary: float
    status: bool
    hire_date: datetime

class Employee(EmployeeBase):
    """ Employee """