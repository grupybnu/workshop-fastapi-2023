from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status

from structlog.typing import FilteringBoundLogger
from structlog import get_logger
from pysondb import PysonDB

from api.schemas.carros import CriarCarroSchema
from api.schemas.padrao import RetornoPadrao


class CadastrarCarroService:


    def __init__(
        self,
        input: CriarCarroSchema,
        db: PysonDB,
        logger: FilteringBoundLogger = get_logger()
    ):
        self.input = input
        self.db = db
        self.logger = logger


    def run(self):
        self.logger.info('Inserindo o carro no banco')

        if self.input.marca == 'Volkswagen':
            self.logger.error('Não aceitamos carros da Volkswagem')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Não aceitamos esse tipo de carro!'
            )
        
        self.db.add(self.input.model_dump())
        self.logger.info('Carro cadastrado com sucesso', carro=self.input.model_dump())

        endpoint_return_content = RetornoPadrao(
            message='Carro cadastado com sucesso!'
        )

        return JSONResponse(
            content=endpoint_return_content.model_dump(),
            status_code=status.HTTP_201_CREATED
        )
    