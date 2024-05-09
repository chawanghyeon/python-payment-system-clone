from project.settings import NUM_SHARDS


class ShardLookupKeyDetermineService:
    @staticmethod
    def determine_shard(order_no: str) -> int:
        return hash(order_no) % NUM_SHARDS
