from structlog.typing import FilteringBoundLogger
from structlog import get_logger


class ListarCarrosService:

    def __init__(self, quantidade: int | None, logger: FilteringBoundLogger = get_logger()):
        self.quantidade = quantidade
        self.logger = logger


    def run(self) -> list[str]:
        lista_carros = [
            'Fiat Uno',
            'Fiat Pálio',
            'Fiat Siena'
        ]

        carros_para_retornar = lista_carros

        if self.quantidade:
            carros_para_retornar = lista_carros[:self.quantidade]
        
        self.logger.info('Retornando os carros', carros=carros_para_retornar)

        return carros_para_retornar
    