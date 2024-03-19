"""Main test for orders interface"""

# Utils imports
import os
import unittest

# Locals imports
from gp.client import Client
from gp.schemas import Order


class TestOrders(unittest.TestCase):
    """Main test for orders interface"""

    def setUp(self):
        """Custom setup"""
        # instantiate the client interface
        self.client: Client = Client()

        # load enviroments variables
        self.access_token: str = os.environ.get('ACCESS_TOKEN')
        self.invalid_token: str = os.environ.get('INVALID_ACCESS_TOKEN')
        self.order_id: str = os.environ.get('ORDER_ID')
        self.url: str = os.environ.get('API_URL')

    def test_get_order_info(self):
        """
        Test get order INFO for orders interface.
        The results comes in the format of:
        {
            "data": {
                "id": "123",
                "type": "Order",
                "attributes": {
                    ...
                    "status": "PENDING",
                    ...
                },
                "links": [{...}]
            }
        }
        """
        # instantiate the orders interface
        order: Order = Order(url=self.url, client=self.client)
        order_id: str = self.order_id
        order_data = order.info(order_id=order_id)

        # assert id in order response is equals to order_id
        assert order_data['data']['data']['attributes']['uuid'] == order_id
        assert order_data['data']['data']['type'] == 'Order'


    def test_create_order(self):
        """Test CREATE for orders interface"""
        order: Order = Order(url=self.url, access_token=self.access_token, client=self.client)
        order_items = [
            {
                "name": "Cuotas Varias",
                "unitPrice": {
                    "currency": "032",
                    "amount": 100.0
                },
                "quantity": 1
            },
        ]
        order_data = order.create(items=order_items)
        # assert id in order response is equals to order_id
        print(order_data)
        assert order_data['data']['data']['attributes']['price']['amount'] == 100
        
    def test_fail_create_order(self):
        """Test a malform request to fail create order"""
        order: Order = Order(url=self.url, access_token=self.invalid_token, client=self.client)
        order_items = [
            {
                "name": "Cuotas Varias",
                "unitPrice": {
                    "currency": "032",
                    "amount": 100.0
                },
                "quantity": 1
            },
        ]
        
        order_data = order.create(items=order_items)
        assert order_data['status'] == 401