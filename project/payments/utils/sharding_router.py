from project.payments.utils.sharding_context_holder import ShardingContextHolder


class ShardingRouter:
    def db_for_read(self, model, **hints):
        shard_lookup_key = ShardingContextHolder.get_shard_lookup_key()
        if shard_lookup_key:
            return f"shard_{shard_lookup_key}"
        return None

    def db_for_write(self, model, **hints):
        shard_lookup_key = ShardingContextHolder.get_shard_lookup_key()
        if shard_lookup_key:
            return f"shard_{shard_lookup_key}"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if objects are from the same shard
        return self.db_for_read(obj1) == self.db_for_read(obj2)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations only for the corresponding shard database
        return db.startswith("shard_")
