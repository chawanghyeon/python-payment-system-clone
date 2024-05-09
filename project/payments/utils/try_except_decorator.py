from functools import wraps
from typing import Any

from rest_framework.response import Response
from rest_framework import status


from project.payments.models.order import Order
from rest_framework.exceptions import ValidationError

from project.payments.utils.sharding_context_holder import ShardingContextHolder


def try_except(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        try:
            result = func(*args, **kwargs)
            return result
        except Order.DoesNotExist:
            order_id = kwargs.get("order_id")
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValueError as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            ShardingContextHolder.clear_context()

    return wrapper
