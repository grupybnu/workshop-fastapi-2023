
class ListarCarrosService:

    def __init__(self, quantidade: int | None):
        self.quantidade = quantidade


    def run(self) -> list[str]:
        lista_carros = [
            'Fiat Uno',
            'Fiat Pálio',
            'Fiat Siena'
        ]

        if self.quantidade:
            return lista_carros[:self.quantidade]
        
        return lista_carros
    