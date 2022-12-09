from fastapi import APIRouter, status

from app.api import healthcheck, employees, beneficiaries, auth, users

"""
Application API routes
"""
api_router = APIRouter()

api_router.include_router(
    healthcheck.router,
    prefix="/healthcheck",
    tags=["Healthcheck"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    auth.router,
    prefix="/login",
    tags=["Login"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Usuarios"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    employees.router,
    prefix="/employees",
    tags=["Employees"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

api_router.include_router(
    beneficiaries.router,
    prefix="/beneficiaries",
    tags=["Beneficiarios"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)