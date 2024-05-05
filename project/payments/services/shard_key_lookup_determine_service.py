from project.settings import NUM_SHARDS, DATABASES


class ShardKeyLookupDetermineService:
    @staticmethod
    def get_shard_key(cls, order_number: str) -> int:
        return hash(order_number) % NUM_SHARDS

    @staticmethod
    def determine_shard(shard_key: int) -> dict:
        if shard_key == 0:
            return DATABASES["db_shard_0"]
        elif shard_key == 1:
            return DATABASES["db_shard_1"]
        elif shard_key == 2:
            return DATABASES["db_shard_2"]
        else:
            return DATABASES["db_shard_3"]
