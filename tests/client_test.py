from unittest import TestCase
from requests.exceptions import ReadTimeout

from apiwatcher_pyclient.client import Client

class ClientTest(TestCase):
    """
    Tests for the client class.
    """

    def initialization_test(self):
        """
        It should be possible to initiliaze the class.
        """
        Client()


    def timeout_test(self):
        """
        Every connection attemt should timeout if timeout is set
        """
        client = Client(api_host="https://httpbin.org",timeout=1)
        client.token = "to_disable_authorization_attempt"

        self.assertRaises(
            ReadTimeout, client.get, "/delay/5"
        )
