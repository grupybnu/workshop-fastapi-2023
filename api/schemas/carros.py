from pydantic import BaseModel


class CriarCarroSchema(BaseModel):
    modelo: str
    marca: str
    ano: int


class AtualizarCarroSchema(BaseModel):
    modelo: str | None = None
    marca: str | None = None
    ano: int | None = None
    