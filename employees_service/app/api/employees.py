from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.employee import Employee, EmployeeCreate, EmployeeUpdate
from app.schemas.user import Usuario
from app.security.auth import get_current_user
from app.db.sgenerator import get_db
from app.repository.crud_employees import repo


router = APIRouter()

@router.get("/", response_model=List[Employee], status_code=status.HTTP_200_OK)
async def get_employees(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    ) -> Any:
    """ Obtiene la lista de empleados """
    try:
        list = repo.get_multi(db=db, skip=skip, limit=limit)
        return list
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.post("/", response_model=Employee, status_code=status.HTTP_200_OK)
async def create_employee(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    new: EmployeeCreate) -> Any:
    """ Registra un nuevo empleado """
    try:
        result = repo.create(db=db, obj_in=new)
        if result:
            return result
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )

@router.put("/{id}", response_model=Employee, status_code=status.HTTP_200_OK)
async def update_employee(
    *,
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int,
    update: EmployeeUpdate) -> Any:
    """ Actualiza un empleado existente"""
    try:
        current = repo.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="empleado no encontrado")
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

@router.delete("/{id}", response_model=Employee, status_code=status.HTTP_200_OK)
async def delete_employee(
    *, 
    db:Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
    id: int) -> Any:
    """ Elimina un empleado existente """
    try:
        current = repo.get(db, id)
        if not current:
            raise HTTPException(status_code=404, detail="empleado no encontrado")
        current = repo.remove(db=db, id=id)
        return current
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error HTTP_500_INTERNAL_SERVER_ERROR {e}"
        )