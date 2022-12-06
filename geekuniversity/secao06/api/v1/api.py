from fastapi import APIRouter

from api.v1.endpoints import artigo
from api.v1.endpoints import usuario


api_route = APIRouter()


api_route.include_router(artigo.router, prefix='/artigos', tags=['artigos'])
api_route.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])