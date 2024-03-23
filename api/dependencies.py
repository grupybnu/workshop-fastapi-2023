from functools import lru_cache

import structlog


@lru_cache
def get_logger() -> structlog.types.FilteringBoundLogger:
    return structlog.get_logger()
