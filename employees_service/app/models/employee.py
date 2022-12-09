from sqlalchemy import text, Boolean, Column, Identity, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(
        Integer,
        Identity(
            start=1,
            increment=1,
            minvalue=1,
            maxvalue=2147483647,
            cycle=False,
            cache=1,
        ),
        primary_key=True,
    )
    name = Column(String(150)) # full name
    # TODO is enumerable
    worker_position = Column(String(150)) # position
    salary = Column(Float(asdecimal=True, precision=2)) # ingress refrente to money
    status = Column(Boolean, default=True) # Active or inactive
    hire_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    beneficiaries = relationship("Beneficiary", cascade="all, delete", back_populates="employee")