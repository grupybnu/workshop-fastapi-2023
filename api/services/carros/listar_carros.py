from structlog.typing import FilteringBoundLogger
from structlog import get_logger
from pysondb import PysonDB


class ListarCarrosService:

    def __init__(
        self,
        quantidade: int | None,
        db: PysonDB,
        logger: FilteringBoundLogger = get_logger()
    ):
        self.quantidade = quantidade
        self.db = db
        self.logger = logger


    def run(self) -> list[str]:
        self.logger.info('Obtendo os carros')

        if self.quantidade:
            carros = self.db.get_all()[:self.quantidade]
        else:
            carros = self.db.get_all()
        
        self.logger.info('Retornando os carros', carros=carros)

        return carros
    