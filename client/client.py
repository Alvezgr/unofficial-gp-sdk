"""Main module client, we define some default behavior from rquests"""

# Utils imports
from requests import Session, Response

# Typing imports
from typing import Optional, Dict, Any


class Client:
    """
    Client interface
    Client is a the implementation fro makings calls to
    geopagos API, we define some default behavior from rquests
    """
    # define https verbs to use
    POST: str = "POST"
    GET: str = "GET"

    def request(
        self,
        method: str,
        url: str,
        headers: Dict[str, str] = None,
        data: Dict[str, str] = None,
        params: Optional[Dict] = None) -> Dict:
        """
        request method to perform HTTP request
        
        Args:
        - method: (str) HTTP method to use
        - url: (str) URL to make the request
        - headers: (Dict) HTTP headers to send in the request
        - params: (Dict) parameters to send in the request

        Returns:
        - api_response: (Dict) response containing the response data and the status code from the API
        """
        current_session: Session = Session()
        with current_session as session:
            api_response: Response = session.request(
                method, url, headers=headers, data=data, params=params
            )

            response: Dict[str, Any] = {
                'status': api_response.status_code,
                'data': api_response.json()
            }
            return response

    def get(self, url: str, headers: Dict[str, str] = None, params: Optional[Dict] = None):
        """
        Perform and http GET request

        Args:
        - url: (str) URL to make the request
        - headers: (Dict) HTTP headers to send in the request
        - params: (Optional, Dict) parameters to send in the request
        
        Returs:
        - api_response: (Dict) response containing the response data and the status code from the API
        """
        api_response: Response = self.request(self.GET, url, headers, params)
        return api_response


    def post(
        self,
        url: str,
        headers: Dict[str, str] = None,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Perform and http GET request

        Args:
        - url: (str) URL to make the request
        - headers: (Dict) HTTP headers to send in the request
        - data: (Dict) HTTP headers to send in the request
        - params: (Optional, Dict) parameters to send in the request
        
        Returs:
        - api_response: (Dict) response containing the response data and the status code from the API
        """
        api_response: Response = self.request(self.POST, url, headers, data, params)
        return api_response
