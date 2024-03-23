from fastapi.responses import JSONResponse
from fastapi import status

from structlog.typing import FilteringBoundLogger
from structlog import get_logger
from pysondb import PysonDB
from pysondb.errors import IdDoesNotExistError

from api.schemas.padrao import RetornoPadrao
from api.schemas.carros import AtualizarCarroSchema


class AtualizarCarroService:

    def __init__(
        self,
        id: int,
        input: AtualizarCarroSchema,
        db: PysonDB,
        logger: FilteringBoundLogger = get_logger()
    ):
        self.id = id
        self.input = input
        self.db = db
        self.logger = logger


    def run(self):
        try:
            self.db.update_by_id(
                id=self.id,
                new_data=self.input.model_dump(exclude_none=True)
            )
            endpoint_return_content = RetornoPadrao(
                message=f'Carro #{self.id} atualizado com sucesso!'
            )
            return JSONResponse(
                content=endpoint_return_content.model_dump(),
                status_code=status.HTTP_200_OK
            )

        except IdDoesNotExistError:
            endpoint_return_content = RetornoPadrao(
                message=f'O carro #{self.id} não foi encontrado na base'
            )
            return JSONResponse(
                content=endpoint_return_content.model_dump(),
                status_code=status.HTTP_404_NOT_FOUND
            )
        