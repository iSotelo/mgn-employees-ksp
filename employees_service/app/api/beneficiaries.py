from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.beneficiary import Beneficiary, BeneficiaryCreate, BeneficiaryUpdate
from app.schemas.user import Usuario
from app.security.auth import get_current_user
from app.db.sgenerator import get_db
from app.repository.crud_beneficiary import repo

router = APIRouter()

@router.get("/", response_model=List[Beneficiary], status_code=status.HTTP_200_OK)
async def get_Beneficiaries(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    ) -> Any:
    """ Obtiene la lista de beneficiarios """
    try:
        list = repo.get_multi(db=db, skip=skip, limit=limit)
        return list
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.post("/", response_model=Beneficiary, status_code=status.HTTP_200_OK)
async def create_beneficiary(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    new: BeneficiaryCreate) -> Any:
    """ Registra un nuevo beneficiario """
    try:
        result = repo.create(db=db, obj_in=new)
        if result:
            return result
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.put("/{id}", response_model=Beneficiary, status_code=status.HTTP_200_OK)
async def update_beneficiary(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int,
    update: BeneficiaryUpdate) -> Any:
    """ Actualiza un beneficiario existente"""
    try:
        current = repo.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="beneficiario no encontrado")
        current = repo.update(
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

@router.delete("/{id}", response_model=Beneficiary, status_code=status.HTTP_200_OK)
async def delete_beneficiary(
    *, 
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int) -> Any:
    """ Elimina un beneficiario existente """
    try:
        current = repo.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="beneficiario no encontrado")
        current = repo.remove(db=db, id=id)
        return current
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )