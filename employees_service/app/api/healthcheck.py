"""
General Healthcheck
"""
from fastapi import APIRouter,status

router = APIRouter()

@router.get("/healthcheck")
def healthcheck():
    """
    Health check end-point
    """
    return status.HTTP_200_OK