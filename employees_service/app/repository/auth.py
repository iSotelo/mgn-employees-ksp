from sqlalchemy.orm import Session
from datetime import timedelta
from pprint import pprint
from app.models.user import User
from fastapi import HTTPException, status
from app.security.hashing import Hash
from pprint import pprint
from app.security.token import create_access_token

def auth_user(usuario, db:Session):
    user = db.query(User).filter(User.username==usuario.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el username: { usuario.username }"
        )
    if not Hash.verify_password(usuario.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contrseña incorrecta!"
        )
    access_token = create_access_token(
        data={"sub": usuario.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}