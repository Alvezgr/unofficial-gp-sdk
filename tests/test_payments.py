"""Main test for payments interface"""

# Utils imports
import os
import unittest

# Locals imports
from gp.client import Client
from gp.schemas import Payment


class TestPayment(unittest.TestCase):
    """Main test for payments interface"""

    def setUp(self):
        """Custom setup"""
        # instantiate the client interface
        self.client: Client = Client()

        # load enviroments variables
        self.access_token: str = os.environ.get('ACCESS_TOKEN')
        self.invalid_token: str = os.environ.get('INVALID_ACCESS_TOKEN')
        self.order_id: str = os.environ.get('ORDER_ID')
        self.url: str = os.environ.get('API_URL')

    def test_create_paymenbt(self):
        """Test CREATE for paymen interface"""
        payment: Payment = Payment(url=self.url, access_token=self.access_token, client=self.client)
        payment_data = {
            "card": {
                "number": "4507990000004905",
                "securityCode": "123",
                "expirationDate": {
                    "month": "08",
                    "year": "30"
                },
                "cardHolder": {
                    "name": "TEST CARD NAME",
                    "identification": {
                        "type": "dni",
                        "number": "12345678"
                    }
                }
            },
            "customer": {
                "name": "TEST CUSTOMER",
                "email": "test@test.com"
            },
            "installmentId": 1
        }
        payment_data = payment.create(order_id=self.order_id, payment_data=payment_data)
        # assert payment data
        assert payment_data['data']['data']['attributes']['price']['amount'] == 100

    def test_fail_create_payment(self):
        """Test fail CREATE for paymen interface"""
        payment: Payment = Payment(
            url=self.url,
            access_token=self.invalid_token,
            client=self.client
        )
        payment_data = {
            "card": {
                "number": "4507990000004905",
                "securityCode": "123",
                "expirationDate": {
                    "month": "08",
                    "year": "30"
                },
                "cardHolder": {
                    "name": "TEST CARD NAME",
                    "identification": {
                        "type": "dni",
                        "number": "12345678"
                    }
                }
            },
            "customer": {
                "name": "TEST CUSTOMER",
                "email": "test@test.com"
            },
            "installmentId": 1
        }
        payment_data = payment.create(order_id=self.order_id, payment_data=payment_data)
        
        # assert payment data
        assert payment_data['data']['errors'][0]["detail"] == "Hubo un error con tu pago, por favor intente nuevamente."
