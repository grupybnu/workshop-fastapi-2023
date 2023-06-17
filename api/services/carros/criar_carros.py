from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status

from api.schemas.carros import CriarCarroSchema


class CadastrarCarroService:


    def __init__(self, input: CriarCarroSchema):
        self.input = input


    def run(self):
        if self.input.marca == 'Volkswagen':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Não aceitamos esse tipo de carro!'
            )
        
        return JSONResponse(
            content={
                'message': 'Carro cadastado com sucesso!'
            },
            status_code=status.HTTP_201_CREATED
        )
    