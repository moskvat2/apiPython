from fastapi import FastAPI, HTTPException, status, Path, Query, Header, Depends

from fastapi.responses import JSONResponse
from fastapi import Response
from typing import List, Optional, Any

from time import sleep

from models import Curso
from models import cursos

def fake_db():
    try:
        print('abrindo conexao com banco de dados')
        sleep(0)
    finally:
        print('finalizando conexao com banco de dados')
        sleep(0)


app = FastAPI(
    title="Geek University",
    description="Minha API",
    version="0.1.0"
)


# default gateway
@app.get('/', description='Check api is running')
async def default():
    return {"api": "API is running"}


@app.get('/cursos',
        description='Return all curses',
        summary='Get all curses in database',
        response_model=List[Curso],
        response_description='Curse find sucessfully')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}',
        description='Return curse by ID',
        summary='Get one curses in database',
        response_model=Curso,
        response_description='Curse find sucessfully')
async def get_curso(curso_id: int = Path(default=None, title='Curse ID',
                                         description='Values range 1 and 2',
                                         gt=0, lt=3), db: Any = Depends(fake_db)):
    # gt = maior que, lt = menor que
    try:
        # try search id curso
        curso = cursos[curso_id - 1]
        return curso
    except KeyError:
        # modified internal server error 500 for 404 not found because id not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='curso not found!')


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)

    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Curse not found with id {curso_id}')


@app.delete('/cursos/{curso_id}',
        description='Delete curse by ID',
        summary='Delete one curse in database',
        response_model=Curso,
        response_description='Curse delted sucessfully')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # obs: existe um bug no JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        # utilizar no lugar Response(status_code=status.HTTP_204_NO_CONTENT)
        # return Response(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Curse not found with id {curso_id}')


if __name__ == "__main__":
    import uvicorn as uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', reload=True)
