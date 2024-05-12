from typing import Any

from django.db.models import Model

from project.payments.utils.sharding_context_holder import ShardingContextHolder


class ShardingRouter:
    def db_for_read(self, model: Model, **hints: Any) -> str | None:
        shard_lookup_key = ShardingContextHolder.get_shard_lookup_key()
        if shard_lookup_key:
            return f"shard_{shard_lookup_key}"
        return None

    def db_for_write(self, model: Model, **hints: Any) -> str | None:
        shard_lookup_key = ShardingContextHolder.get_shard_lookup_key()
        if shard_lookup_key:
            return f"shard_{shard_lookup_key}"
        return None

    def allow_relation(self, obj1: Model, obj2: Model, **hints: Any) -> bool:
        # Allow relations if objects are from the same shard
        return self.db_for_read(obj1) == self.db_for_read(obj2)

    def allow_migrate(
        self, db: str, app_label: str, model_name: str | None = None, **hints: Any
    ) -> bool:
        return True
