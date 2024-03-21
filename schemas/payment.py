"""Payment main module"""

# typings imports
from typing import Dict

# Utils imports
from json.encoder import JSONEncoder
from requests_toolbelt.multipart.encoder import MultipartEncoder

# App main imports
from gp.client import Client


class Payment:
    """
    Represents a payment and provides methods to interact with payment data.
    """

    def __init__(self, access_token: str, url: str, client: Client) -> None:
        """
        Initializes an Payment object.

        Parameters:
        - access_token (str): The access token for authentication.
        - app_url (str): The URL of the application, any application of geopagos such as:
            (https://api.globalgetnet.com.ar, https://api.viumi.com.ar, ... etc)
        - client (Client): An instance of the Client class for making HTTP requests.

        Attributes:
        - app_url (str): The URL of the application.
        - access_token (str): The access token for authentication.
        - client (Client): An instance of the Client class for making HTTP requests.
        - header (Dict[str, str]): HTTP headers including Content-Type and Authorization.
        """
        self.url: str = url
        self.access_token: str = access_token
        self.client: Client = client
        self.header: Dict[str, str] = {
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Bearer {access_token}",
        }

    def create(self, order_id: str, payment_data: Dict) -> Dict:
        """
        Create a payment for a specific order.

        Parameters:
        - order_id (str): The ID of the order for which the payment is being created.
        - payment_data (Dict): A dictionary containing payment data to be created
            you shuld never use this method in a web application, we are dealing with
            card sesitive data and shuld never reach your server, use the checkout
            url returned in the order object, this is used by GUI and dev expiremental unique.

        Returns:
        - Dict: A dictionary containing the response from the payment creation request.
        """

        if payment_data is not None:
            payment_data = JSONEncoder().encode(payment_data)
        return self.client.post(
            f"{self.url}/api/v2/orders/{order_id}/payments", header=self.header
        )

    def refund(self, refund_data: Dict) -> Dict:
        """
        Request a refund for a payment.

        Parameters:
        - refund_data (Dict): A dictionary containing refund data.

        Returns:
        - Dict: A dictionary containing the response from the refund request.
        """
        if refund_data is not None:
            refund_data = JSONEncoder().encode(refund_data)
        return self.client.post(f"{self.url}/api/v2/refunds", header=self.header)

    def installments(self, merchant_data: Dict) -> Dict:
        """
        Request the posible isntallments

        Paramenters:
        - merchant_data (Dict) A dictionary containing installment request data
        the merchant data should look like:
            mercant_data = {
                "bin": card_bin_number,
                "total": total_amount,
                "mode": "ECOMMERCE",
                "acountId": acount_id_app,
                "cardNumber": card_number
            }

        Returns:
        - Dict: A dictionary containing the response from the refund request.
        """
        if merchant_data is not None:
            merchant_data_encoded: MultipartEncoder = MultipartEncoder(fields=merchant_data)
            self.header: Dict[str, str] = {"Content-Type": merchant_data_encoded.content_type}

        return self.client.post(f"{self.url}/api/checkout/getInstallments.json", headers=self.header, data=merchant_data_encoded)
