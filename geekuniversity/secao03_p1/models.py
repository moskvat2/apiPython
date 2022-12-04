from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    # validações
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 10:
            raise ValueError('Total de aulas incompleta')

        return value
    
    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('Carga horária incompleta')

        return value


# list example without database server
cursos = [
    Curso(id=1, titulo='Developer fo dummys', aulas=67, horas=67),
    Curso(id=2, titulo='Algorithm', aulas=30, horas=45)
]