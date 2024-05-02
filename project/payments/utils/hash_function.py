def calculate_hash(key, num_shards):
    """Calculates the hash value for a given key using modulo operation.

    :param key: The key to be hashed.
    :type key: str
    :param num_shards: The number of shards or partitions.
    :type num_shards: int
    :return: The shard number where the key belongs.
    :rtype: int
    """
    hash_value = hash(key) % num_shards
    return hash_value
