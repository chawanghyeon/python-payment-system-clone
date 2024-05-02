from project.settings import DATABASES


def get_shard(sharding_key: int) -> dict:
    if sharding_key == 0:
        return DATABASES["db_shard_0"]
    elif sharding_key == 1:
        return DATABASES["db_shard_1"]
    elif sharding_key == 2:
        return DATABASES["db_shard_2"]
    else:
        return DATABASES["db_shard_3"]
