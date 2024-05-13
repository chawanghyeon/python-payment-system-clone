import pytest

from project.payments.utils.sharding_target_decorator import sharding_target


def test_sharding_target_decorator_called_with_correct_arguments():
    @sharding_target
    def my_function(arg1, arg2):
        assert arg1 == 10
        assert arg2 == "test"

    my_function(10, "test")


def test_sharding_target_decorator_returns_expected_result():
    @sharding_target
    def my_function(arg1, arg2):
        return arg1 + arg2

    result = my_function(5, 10)
    assert result == 15


def test_sharding_target_decorator_raises_exception_on_invalid_argument():
    @sharding_target
    def my_function(arg1):
        if arg1 < 0:
            raise ValueError("Invalid argument")

    with pytest.raises(ValueError):
        my_function(-5)


def test_sharding_target_decorator_called_multiple_times():
    @sharding_target
    def my_function(arg1):
        assert arg1 > 0

    my_function(10)
    my_function(20)
    my_function(30)


def test_sharding_target_decorator_called_with_keyword_arguments():
    @sharding_target
    def my_function(arg1, arg2):
        assert arg1 == 5
        assert arg2 == "test"

    my_function(arg1=5, arg2="test")
