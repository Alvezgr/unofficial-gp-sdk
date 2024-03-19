"""Order main module."""

# Utils imports
from json.encoder import JSONEncoder

# Typing imports
from typing import Dict, Any

# Local imports
from gp.client import Client


class Order:
    """
    Main order interface
    Order represent a order in the geopagos API
    """
    def __init__(self, url: str, access_token: str = None, client: Client = None) -> None:
        """Initialize an Order objectr.
        Args:
            access_token (str): Access token
            url (str): URL
            client (Client): Client

        Attrs:
            headers: (Dict) HTTP headers to send including Content-Type and Authorization
        """

        self.url: str = url
        self.client: Client = client
        self.access_token: str = access_token

    def info(self, order_id: str) -> Dict[str, Any]:
        """Get order information.
        Args:
            order_id (str): Order ID

        Returns:
            Dict[str, Any]: Order
        """
        headers: Dict[str, str] = {
            "Content-Type": "application/vnd.api+json",
        }
        return self.client.get(f"{self.url}/api/v2/orders/{order_id}", headers=headers)

    def create(self, items: Dict[str, any]) -> Dict[str, Any]:
        """Create a new order.

        Arg:
            items (Dict[str, any]): Items of a order

        Returns:
            Dict[str, Any]: Order
        """
        headers: Dict[str, str] = {
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Bearer {self.access_token}"
        }
        if items is not None:
            order_data = {
                "data": {
                    "attributes": { "items": items }
                }
            }
            order_data = JSONEncoder().encode(order_data)
        return self.client.post(f"{self.url}/api/v2/orders", data=order_data, headers=headers)