from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    # Configuracoes gerais utilizadas na aplicacao
    API_V1_STR: str = '/api/v1'
    DB_URL = "mysql+asyncmy://root:root@172.16.0.99/faculdade?charset=utf8mb4"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
