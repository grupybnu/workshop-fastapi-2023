from fastapi.responses import JSONResponse
from fastapi import status
from structlog.typing import FilteringBoundLogger
from structlog import get_logger

from pysondb import PysonDB
from pysondb.errors import IdDoesNotExistError


class DetalhesCarroService:

    def __init__(
        self,
        id: str,
        db: PysonDB,
        logger: FilteringBoundLogger = get_logger()
    ):
        self.id = id
        self.db = db
        self.logger = logger

    def get_carro_completo(self) -> dict | JSONResponse:
        try:
            carro = self.db.get_by_id(self.id)
            self.logger.info('Carro obtido com sucesso!', carro=carro)
            return carro
        
        except IdDoesNotExistError:
            return JSONResponse(
                content={
                    'message': 'Carro não encontrado!'
                },
                status_code=status.HTTP_404_NOT_FOUND
            )
    
    def get_marca(self) -> dict | JSONResponse:
        try:
            carro = self.db.get_by_id(self.id)
            self.logger.info('Carro obtido com sucesso!', carro=carro)
            return {'value': carro.get('marca')}
        
        except IdDoesNotExistError:
            return JSONResponse(
                content={
                    'message': 'Carro não encontrado!'
                },
                status_code=status.HTTP_404_NOT_FOUND
            )
