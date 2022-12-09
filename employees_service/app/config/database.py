from os import getenv
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    postgres_host: Optional[str]
    postgres_port: str = "5432"
    postgres_password: Optional[str]
    postgres_user: Optional[str]
    postgres_db: Optional[str]

    @property
    def postgres_uri(self):
        self.postgres_host = getenv("POSTGRES_SERVER")
        self.postgres_port = getenv("POSTGRES_PORT", 5432)
        self.postgres_user = getenv("POSTGRES_USER")
        self.postgres_password = getenv("POSTGRES_PASSWORD")
        self.postgres_db = getenv("POSTGRES_DB")
        
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    @property
    def sqlite_uri(self):
        return "sqlite:///./db.sqlite3"

settings = Settings()