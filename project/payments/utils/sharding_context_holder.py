class ShardingContextHolder:
    def __init__(self):
        self._sharding_context = None

    def set_sharding_context(self, sharding_context):
        self._sharding_context = sharding_context

    def get_sharding_context(self):
        return self._sharding_context

    def clear_context(self):
        self._sharding_context = None
