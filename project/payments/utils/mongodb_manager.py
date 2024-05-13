from typing import Any

from pymongo import MongoClient

from project.payments.models.order import Order


class MongoDbManager:
    _instance = None
    client: MongoClient[Any] = MongoClient(host="localhost", port=27017)
    database = client["MyApplicationDB"]["MyApplicationCollection"]

    def __new__(cls, *args: list[Any], **kwargs: dict[Any, Any]) -> "MongoDbManager":
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def get_order(cls, user_id: int, order_no: str) -> dict[str, Any]:
        order = cls.database.find_one({"user_id": user_id, "order_no": order_no})
        if order is None:
            raise Order.DoesNotExist
        return order

    def add_order_on_collection(cls, data: dict[str, Any]) -> Any | None:
        return cls.database.insert_one(data)


mongo_db_manager = MongoDbManager()
