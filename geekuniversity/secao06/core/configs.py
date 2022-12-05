from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    # Configuracoes gerais utilizadas na aplicacao
    API_V1_STR: str = '/api/v1'
    DB_URL = "mysql+asyncmy://root:root@172.16.0.99/faculdade?charset=utf8mb4"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '-bZEK69at2_tzk-Q7rMm4h4DQ7IpYGsrm9gJVzLAHU4'
    """
        import secrets
        token: str secrets.token_urlsafe(32)
        # abra o console python e rode os comandos acima para gera um token
        # e cole em JWT_SECRET
    """
    
    ALGORITHM: str = 'HS256'
    
    # 60 min * 24 hrs * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()
