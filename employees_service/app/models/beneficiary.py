from sqlalchemy import text, Boolean, Column, Identity, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.base import Base

class Beneficiary(Base):
    __tablename__ = "beneficiaries"
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
    relationship_to_employee = Column(String(150)) # relationship with the employee
    birthday = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    gender = Column(String(10)) # male/female
    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="beneficiaries")