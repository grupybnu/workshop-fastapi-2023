from fastapi.responses import JSONResponse
from fastapi import status

from api.schemas.padrao import RetornoPadrao
from api.schemas.carros import AtualizarCarroSchema


class AtualizarCarroService:

    def __init__(self, id: int, input: AtualizarCarroSchema):
        self.id = id
        self.input = input


    def run(self):
        endpoint_return_content = RetornoPadrao(
            message=f'Carro #{self.id} atualizado com sucesso!'
        )
        return JSONResponse(
            content=endpoint_return_content.dict(),
            status_code=status.HTTP_200_OK
        )
    