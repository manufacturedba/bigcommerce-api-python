class RequestException(RuntimeError):
    """There was an ambiguous exception that occurred while handling your
    request."""
    
    
class MissingStoreAddress(RequestException, ValueError):
    """The URL for a store must be provided"""
   
    
class MissingCredentials(RequestException, ValueError):
    """Authentication must be provided"""
