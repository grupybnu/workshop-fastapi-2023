# Oficina FastAPI GruPy Blumenau 2023

![image](https://github.com/jjpaulo2/oficina-fastapi-grupy-blumenau-2023/assets/22819523/74f8c993-a2f4-47e6-a535-29a8e40ff0c9)

Código-fonte da API RESTful construída na oficina de FastAPI realizada no *GruPy Blumenau* no dia *17/06/2023*.

### Links interessantes
- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Apresentação usada da oficina](https://speakerdeck.com/jjpaulo2/fastapi-na-pratica)

## Iniciando no FastAPI

### Instalando as dependências

Crie um ambiente virtual do Python. Isto é importante para isolar as dependências do projeto, das dependências do seu sistema operacional.

```shell
python -m venv .venv
```

Isso irá criar uma pasta `.venv` dentro da sua pasta atual.

Agora, ative o ambiente virtual.

```shell
source ./.venv/bin/activate
```

Instale o FastAPI propriamente dito.

```shell
pip install fastapi
```

Instale o Uvicorn. Usaremos ele para rodar a nossa aplicação.

```shell
pip install "uvicorn[standard]"
```

Pronto, você já pode dar inicio ao desenvolvimento.

### Nossa primeira aplicação

Crie um arquivo chamado `app.py` e coloque o seguinte conteúdo dentro dele.

```python
from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

Para executar a aplicação, rode o comando abaixo no terminal.

```shell
uvicorn main:app --reload
```

Agora, navegue para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

![image](https://github.com/jjpaulo2/oficina-fastapi-grupy-blumenau-2023/assets/22819523/3fa832d7-f23f-4c9d-ae1a-f66a41e19b7a)

## O código feito durante a oficina

O código que fizemos durante a oficina está dentro do módulo [`api`](./api). 

```
api
├── services
│   └── carros
│       ├── listar_carros.py
│       ├── detalhes_carro.py
│       ├── criar_carros.py
│       └── atualizar_carros.py
├── schemas
│   ├── padrao.py
│   └── carros.py
├── routes
│   └── carros.py
├── __init__.py
├── dependencies.py
└── app.py
```

A versão do Python usada foi a `3.11.3` e está declarada no arquivo [`.python-version`](./.python-version). Você pode instalá-la diretamente pelo [site do Python](https://www.python.org/downloads/release/python-3113/), ou usando [`pyenv`](https://github.com/pyenv/pyenv), como abaixo.

```shell
pyenv install $(pyenv local)
```

Para executá-lo, crie um ambiente virtual e instale as dependências listadas no arquivo [`requirements.txt`](./requirements.txt).

```shell
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

Agora é só rodar o projeto.

```shell
uvicorn api.app:app --reload
```

Agora, é só navegar para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

![image](https://github.com/jjpaulo2/oficina-fastapi-grupy-blumenau-2023/assets/22819523/d373bc63-5be9-415c-948e-448005d2452b)
