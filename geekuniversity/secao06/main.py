from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_route


app = FastAPI(title='Cursos API - FastAPI SQL Model - Buddy CICD - 2022')
app.include_router(api_route, prefix=settings.API_V1_STR) # return constant /api/v1


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=5000,
                log_level='info', reload=True)
