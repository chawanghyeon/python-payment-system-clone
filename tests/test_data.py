test_data = {
    "order_pay_method": {
        "card": False,
        "card_receipt": False,
        "cash": False,
        "amount_paid": 0,
    },
    "order_memo": {"memo": "test"},
    "delivery": {
        "regional_code": 1,
        "delivery_address": "test",
    },
    "line_items": [
        {
            "product_id": 1,
            "name": "test",
            "quantity": 1,
            "price": 100,
            "line_item_options": [
                {"name": "test", "price": 100},
                {"name": "test2", "price": 100},
            ],
        },
        {
            "product_id": 2,
            "name": "test2",
            "quantity": 2,
            "price": 200,
            "line_item_options": [
                {"name": "test", "price": 100},
                {"name": "test2", "price": 100},
            ],
        },
    ],
    "seller_summary": {"name": "test", "address": "test"},
    "charge_lines": [
        {"description": "test", "amount": 100, "status": "PRODUCT"},
        {"description": "test2", "amount": 100, "status": "SHIPPING"},
    ],
}
