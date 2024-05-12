import threading


class ShardingContextHolder:
    _context_holder = threading.local()

    @classmethod
    def set_sharding_context(cls, shard_key: str, shard_lookup_key: int) -> None:
        cls._context_holder.sharding_context = {
            "shard_key": shard_key,
            "shard_lookup_key": shard_lookup_key,
        }

    @classmethod
    def get_shard_lookup_key(cls) -> int | None:
        if hasattr(cls._context_holder, "sharding_context"):
            return cls._context_holder.sharding_context.get("shard_lookup_key")
        return None

    @classmethod
    def clear_context(cls) -> None:
        if hasattr(cls._context_holder, "sharding_context"):
            del cls._context_holder.sharding_context
