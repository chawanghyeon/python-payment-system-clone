import pytest

from project.payments.utils.mongodb_manager import MongoDbManager


@pytest.fixture
def mongo_db_manager():
    return MongoDbManager()


def test_get_order(mongo_db_manager):
    # Test case for getting an order
    user_id = 123
    order_no = "ABC123"
    order = mongo_db_manager.get_order(user_id, order_no)
    assert isinstance(order, Order)
    assert order.user_id == user_id
    assert order.order_no == order_no


def test_add_order_on_collection(mongo_db_manager):
    # Test case for adding an order to the collection
    data = {"user_id": 123, "order_no": "ABC123", "amount": 100.0}
    result = mongo_db_manager.add_order_on_collection(data)
    assert result is not None


def test_singleton_instance():
    # Test case for checking if the MongoDbManager is a singleton
    mongo_db_manager_1 = MongoDbManager()
    mongo_db_manager_2 = MongoDbManager()
    assert mongo_db_manager_1 is mongo_db_manager_2
