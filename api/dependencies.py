from functools import lru_cache

import structlog

from pysondb import PysonDB
from api.settings import DB_FILE


@lru_cache
def get_logger() -> structlog.types.FilteringBoundLogger:
    return structlog.get_logger()


@lru_cache
def get_db() -> PysonDB:
    return PysonDB(DB_FILE)
