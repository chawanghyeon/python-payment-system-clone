from functools import wraps
from typing import Any

from project.payments.services.shard_lookup_key_determine_service import (
    ShardLookupKeyDetermineService,
)
from project.payments.utils.sharding_context_holder import ShardingContextHolder


def sharding_target(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        order_number: str = kwargs.get("order_number", "")
        if order_number is None:
            raise ValueError("order_number is required")

        shard_lookup_key = ShardLookupKeyDetermineService.determine_shard(order_number)
        if shard_lookup_key is None:
            raise ValueError("shard_lookup_key is not found")

        try:
            ShardingContextHolder.set_sharding_context(order_number, shard_lookup_key)
            result = func(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            ShardingContextHolder.clear_context()

        return result

    return wrapper
