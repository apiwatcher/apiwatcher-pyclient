from unittest import TestCase
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
