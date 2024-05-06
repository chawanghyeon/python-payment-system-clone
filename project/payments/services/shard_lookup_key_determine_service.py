from project.settings import NUM_SHARDS, DATABASES


class ShardLookupKeyDetermineService:
    @staticmethod
    def determine_shard(user_id: int) -> dict | None:
        shard_key = user_id % NUM_SHARDS
        return DATABASES.get(f"shard_{shard_key}")
