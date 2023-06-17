
class DetalhesCarroService:

    def __init__(self, id: int):
        self.id = id

    def get_carro_completo(self) -> dict:
        return {
            'id': self.id,
            'marca': 'Fiat',
            'modelo': 'Uno',
            'ano': 2015
        }
    
    def get_marca(self) -> dict:
        return {
            'id': self.id,
            'marca': 'Fiat'
        }
    