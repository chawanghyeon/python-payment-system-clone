from project.payments.utils.sharding_context_holder import ShardingContextHolder


def test_set_sharding_context():
    ShardingContextHolder.set_sharding_context("shard_key", 123)
    assert ShardingContextHolder.get_shard_lookup_key() == 123


def test_get_shard_lookup_key():
    ShardingContextHolder.set_sharding_context("shard_key", 456)
    assert ShardingContextHolder.get_shard_lookup_key() == 456


def test_clear_context():
    ShardingContextHolder.set_sharding_context("shard_key", 789)
    ShardingContextHolder.clear_context()
    assert ShardingContextHolder.get_shard_lookup_key() is None
