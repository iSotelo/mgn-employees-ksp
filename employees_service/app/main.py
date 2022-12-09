import uvicorn
import secure
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import OperationalError
from retrying import retry
from fastapi.middleware.cors import CORSMiddleware

from app.utils.exceptions import DeployError
from app.routes.router import api_router
from app.db.session import SessionLocal

# Database configuration
# def create_tables():
#     Base.metadata.create_all(bind=engine)
# create_tables()

secure_headers = secure.Secure()

app = FastAPI(
    title="Employees Service",
    description="Web service for the management of employees and beneficiaries",
    version="0.1.0",
)

## config CORS Policy, only in dev anviroment
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
@retry(
    retry_on_result=DeployError.db_starting_up,
    wait_fixed=10000,
    stop_max_attempt_number=3,
)
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    except OperationalError as e:
        DeployError.db_starting_up(e)
    finally:
        request.state.db.close()
    return response

@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response

app.include_router(api_router)

# if __name__=="__main__":
#     uvicorn.run("main:app", port=3000, reload=True)