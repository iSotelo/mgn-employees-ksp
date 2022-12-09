from app.repository.crud_base import CRUDBase
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):
    pass

repo = CRUDEmployee(Employee)