from fastapi import APIRouter

from api.v1.endpoints import curso


api_router = APIRouter()

# router formará /api/v1/{prefix} = /api/v1/cursos
api_router.include_router(curso.router, prefix='/cursos', tags=["cursos"])
