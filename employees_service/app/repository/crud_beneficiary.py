from app.repository.crud_base import CRUDBase
from app.models.beneficiary import Beneficiary
from app.schemas.beneficiary import BeneficiaryCreate, BeneficiaryUpdate

class CRUDBeneficiary(CRUDBase[Beneficiary, BeneficiaryCreate, BeneficiaryUpdate]):
    pass

repo = CRUDBeneficiary(Beneficiary)