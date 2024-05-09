from datetime import datetime
from functools import wraps
from random import randint
from typing import Any

from project.payments.services.shard_lookup_key_determine_service import (
    ShardLookupKeyDetermineService,
)
from project.payments.utils.sharding_context_holder import ShardingContextHolder
from django.utils.crypto import get_random_string


def retrieve_order_no(*args: Any, **kwargs: Any, func) -> str:
    order_no = kwargs.get("order_no")
    
    if func.__name__ == "create_order":
        data = kwargs.get("data")
        address = data.dilivery.delivery_address 
        reginal_code = data.dilivery.reginal_code
        current_date = datetime.now().strftime("%Y%m%d")

        random_string = get_random_string(length=6, allowed_chars=address)
        order_no = f"{current_date}-{reginal_code}-{random_string}"
    
    if order_no is None:
        raise ValueError("order_no is required")
    
    return order_no


def sharding_target(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        order_no = retrieve_order_no(*args, **kwargs, func=func)

        shard_lookup_key = ShardLookupKeyDetermineService.determine_shard(order_no)

        ShardingContextHolder.set_sharding_context(order_no, shard_lookup_key)
        return func(*args, **kwargs)

    return wrapper
