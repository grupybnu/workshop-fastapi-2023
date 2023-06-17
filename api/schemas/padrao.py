from pydantic import BaseModel


class RetornoPadrao(BaseModel):
    message: str


class ErroPadrao(BaseModel):
    erro: str
    