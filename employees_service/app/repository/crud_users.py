from app.repository.crud_base import CRUDBase
from app.models.user import User
from app.schemas.user import UsuarioCreate, UsuarioUpdate

class CRUDUser(CRUDBase[User, UsuarioCreate, UsuarioUpdate]):
    pass

usuario = CRUDUser(User)