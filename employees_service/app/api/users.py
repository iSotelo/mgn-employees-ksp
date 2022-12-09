from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import Usuario, UsuarioCreate, UsuarioUpdate
from app.db.sgenerator import get_db
from app.repository.crud_users import usuario
from app.security.auth import get_current_user
from app.security.hashing import Hash

router = APIRouter()

@router.get("/", response_model=List[Usuario], status_code=status.HTTP_200_OK)
async def get_users(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    ) -> Any:
    """ Obtiene la lista de usurios """
    try:
        list = usuario.get_multi(db=db, skip=skip, limit=limit)
        return list
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.post("/", response_model=Usuario, status_code=status.HTTP_200_OK)
async def create_user(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    new: UsuarioCreate) -> Any:
    """ Registra un nuevo usuario """
    try:
        new.password = Hash.hash_password(new.password)
        result = usuario.create(db=db, obj_in=new)
        if result:
            return result
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.put("/{id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def update_user(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int,
    update: UsuarioUpdate) -> Any:
    """ Actualiza un usuario existente"""
    try:
        current = usuario.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        update.password = Hash.hash_password(update.password)
        current = usuario.update(
            db=db,
            db_obj=current,
            obj_in=update
        )
        return current
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.delete("/{id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def delete_user(
    *, 
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int) -> Any:
    """ Elimina un usuario existente """
    try:
        current = usuario.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        current = usuario.remove(db=db, id=id)
        return current
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )