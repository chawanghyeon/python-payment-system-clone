from functools import wraps
from typing import Any

from project.payments.services.shard_lookup_key_determine_service import (
    ShardLookupKeyDetermineService,
)
from project.payments.utils.sharding_context_holder import ShardingContextHolder
from rest_framework.response import Response
from rest_framework import status


def sharding_target(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        user_id = kwargs.get("user_id")
        if user_id is None:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        shard_lookup_key = ShardLookupKeyDetermineService.determine_shard(user_id)
        if shard_lookup_key is None:
            return Response(
                "shard_lookup_key is required", status=status.HTTP_400_BAD_REQUEST
            )

        try:
            ShardingContextHolder.set_sharding_context(user_id, shard_lookup_key)
            result = func(*args, **kwargs)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            ShardingContextHolder.clear_context()

        return result

    return wrapper
