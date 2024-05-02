from project.payments.models.order import Order


class OrderService:
    @classmethod
    def create_order(cls, order_id: int, amount: float) -> None:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        shard.create_order(order_id, amount)

    @classmethod
    def read_order(cls, order_id: int) -> Order:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        return shard.get_order(order_id)

    @classmethod
    def update_order(cls, order_id: int, amount: float) -> None:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        shard.update_order(order_id, amount)

    @classmethod
    def delete_order(cls, order_id: int) -> None:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        shard.delete_order(order_id)
