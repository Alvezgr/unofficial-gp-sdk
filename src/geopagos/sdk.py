"""SDK module."""

# App main imports
from geopagos.client import Client
from geopagos.schemas import Order, Payment


class SDK:
    """
    SDK module for interacting with the API.

    This class provides high-level methods for accessing different API endpoints.
    """

    def __init__(self, access_token: str, url: str) -> None:
        """
        Initializes the SDK.

        Parameters:
        - access_token (str): The access token for authentication.
        - url (str): The base URL of the application's API.

        Attributes:
        - access_token (str): The access token for authentication.
        - url (str): The base URL of the application's API.
        - client (Client): An instance of the Client class for making HTTP requests.
        """
        self.access_token: str = access_token
        self.url: str = url
        self.client: Client = Client()

    def order(self) -> Order:
        """
        Create an instance of the Order class with the provided access token and app URL.

        Returns:
        - Order: An instance of the Order class.
        """
        return Order(self.access_token, self.url, self.client)

    def payment(self) -> Payment:
        """
        Create an instance of the Payment class with the provided access token and app URL.

        Returns:
        - Payment: An instance of the Payment class.
        """
        return Payment(self.access_token, self.url, self.client)

