
class ApiwatcherClientException(Exception):
    """
    Generic exception for Apiwatcher Pyclient.

    Every other exception should inherit from this one. On the other hand it
    does not mean than other exception can not be raised.
    """
    pass
