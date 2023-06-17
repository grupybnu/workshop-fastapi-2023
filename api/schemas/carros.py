from pydantic import BaseModel


class CriarCarroSchema(BaseModel):
    modelo: str
    marca: str
    ano: int


class AtualizarCarroSchema(BaseModel):
    modelo: str | None
    marca: str | None
    ano: int | None
    