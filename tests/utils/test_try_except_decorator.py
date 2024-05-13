import pytest
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from project.payments.utils.try_except_decorator import try_except


def test_try_except_decorator():
    @try_except
    def divide(a, b):
        return a / b

    # Test case 1: Valid division
    result = divide(10, 2)
    assert result == 5

    # Test case 2: Division by zero
    with pytest.raises(ValidationError) as exc_info:
        divide(10, 0)
    assert str(exc_info.value) == "Division by zero is not allowed."

    # Test case 3: Exception raised within the decorated function
    @try_except
    def raise_exception():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError) as exc_info:
        raise_exception()
    assert str(exc_info.value) == "Something went wrong"

    # Test case 4: Decorator applied to a function that returns a Response object
    @try_except
    def return_response():
        return Response({"message": "Success"}, status=status.HTTP_200_OK)

    result = return_response()
    assert result.status_code == status.HTTP_200_OK
    assert result.data == {"message": "Success"}

    # Test case 5: Decorator applied to a function that returns None
    @try_except
    def return_none():
        return None

    result = return_none()
    assert result is None

    # Test case 6: Decorator applied to a function that raises a different exception
    @try_except
    def raise_custom_exception():
        raise Exception("Custom exception")

    with pytest.raises(Exception) as exc_info:
        raise_custom_exception()
    assert str(exc_info.value) == "Custom exception"
