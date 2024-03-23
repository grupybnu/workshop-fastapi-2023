from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import status, Depends
from structlog.typing import FilteringBoundLogger
from pysondb import PysonDB

from api.dependencies import get_logger, get_db
from api.schemas.carros import AtualizarCarroSchema, CriarCarroSchema
from api.schemas.padrao import ErroPadrao, RetornoPadrao

from api.services.carros.atualizar_carros import AtualizarCarroService
from api.services.carros.criar_carros import CadastrarCarroService
from api.services.carros.detalhes_carro import DetalhesCarroService
from api.services.carros.listar_carros import ListarCarrosService



carros_router = APIRouter(
    prefix="/carros"
)


@carros_router.get("/")
def list_carros(
    logger: Annotated[FilteringBoundLogger, Depends(get_logger)],
    db: Annotated[PysonDB, Depends(get_db)],
    quantidade: int | None = None
):
    service = ListarCarrosService(quantidade, db, logger)
    return service.run()


@carros_router.get('/{carro_id}')
def get_carro(
    carro_id: str,
    logger: Annotated[FilteringBoundLogger, Depends(get_logger)],
    db: Annotated[PysonDB, Depends(get_db)]
):
    service = DetalhesCarroService(carro_id, db, logger)
    return service.get_carro_completo()


@carros_router.get('/{carro_id}/marca')
def get_marca_carro(
    carro_id: str,
    logger: Annotated[FilteringBoundLogger, Depends(get_logger)],
    db: Annotated[PysonDB, Depends(get_db)]
):
    service = DetalhesCarroService(carro_id, db, logger)
    return service.get_marca()


@carros_router.post('/')
def cadastrar_carro(
    input: CriarCarroSchema,
    logger: Annotated[FilteringBoundLogger, Depends(get_logger)],
    db: Annotated[PysonDB, Depends(get_db)],
):
    service = CadastrarCarroService(input, db, logger)
    return service.run()


@carros_router.patch('/{carro_id}', responses={
    status.HTTP_200_OK: {
        'model': RetornoPadrao 
    },
    status.HTTP_400_BAD_REQUEST: {
        'model': ErroPadrao
    }
})
def atualizar_carro(
    carro_id: str,
    input: AtualizarCarroSchema,
    logger: Annotated[FilteringBoundLogger, Depends(get_logger)],
    db: Annotated[PysonDB, Depends(get_db)]
):
    service = AtualizarCarroService(carro_id, input, db, logger)
    return service.run()
