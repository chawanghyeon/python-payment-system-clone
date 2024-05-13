import pytest
from django.db.models import Model

from project.payments.utils.sharding_router import ShardingRouter


@pytest.fixture
def sharding_router():
    return ShardingRouter()


def test_db_for_read(sharding_router):
    model = Model()
    db = sharding_router.db_for_read(model)
    assert db is None  # Add your assertion here


def test_db_for_write(sharding_router):
    model = Model()
    db = sharding_router.db_for_write(model)
    assert db is None  # Add your assertion here


def test_allow_relation(sharding_router):
    obj1 = Model()
    obj2 = Model()
    allow = sharding_router.allow_relation(obj1, obj2)
    assert allow is True  # Add your assertion here


def test_allow_migrate(sharding_router):
    db = "default"
    app_label = "myapp"
    model_name = "MyModel"
    allow = sharding_router.allow_migrate(db, app_label, model_name)
    assert allow is True  # Add your assertion here
