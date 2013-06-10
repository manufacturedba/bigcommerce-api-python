"""
This module provides an object-oriented wrapper around the BigCommerce V2 API
for use in Python projects or via the Python shell.

"""

import base64
import simplejson as json
import requests

API_PROTOCOL = 'https'
API_HOST = ''
API_PATH = '/api/v2'
API_USER = ''
API_KEY  = ''

class Connection(object):
    host = API_HOST
    base_path = API_PATH
    user = API_USER
    api_key = API_KEY
    protocol = API_PROTOCOL
    
    if not self.host:
        raise MissingStoreAddress("No store address was provided")
            
    def request_json(self, method, path, data=None):
        response = self.request(method, path, data)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return {'Error':response.json()}

    def build_request_headers(self):
        
        if not (self.user or self.api_key):
            raise MissingCredentials("Must provide authentication")
            
        auth = base64.b64encode(self.user + ':' + self.api_key)
        return {'Authorization': 'Basic ' + auth,  'Accept' : 'application/json;0.9'}

    def request(self, method, path, body=None):
        
        url = self.protocol + '://' + self.host + self.base_path + path + '.json'
        headers = self.build_request_headers()
        
        if body:
            body = json.dumps(body)
            headers['Content-Type'] = 'application/json'
            if method == "PUT":
                return requests.put(url,body,headers=headers)
            else:
                return requests.post(url, body, headers=headers)
        elif method == "DELETE":
            return requests.delete(url, headers=headers)           
        else:
            return requests.get(url, headers=headers)



class Resource(object):
    """Base class representing BigCommerce resources"""

    client = Connection()

    def __init__(self, fields=None):
        pass

    def __iter__(self):
        return self
    
    def filtering(self, filters):
        params = "?"
        if type(filters) == dict:
            for key, value in filters.items():
                filter_string = '%s=%s&' % (key, value)
                params += filter_string
            return params
        else:
            return params
                
    def get(self, filters=None):
        """Fetch all resources"""
        resource_list = self.client.request_json('GET', self.ext + self.filtering(filters))
        return resource_list
   
    def get_by_id(self, ID):
        """Fetch resource by id"""
        resource = self.client.request_json('GET', self.ext + '/' + str(ID))
        self.selected = ID
        return resource
    
    def create(self, payload):
        """Create new resource"""
        return self.client.request_json('POST', self.ext, payload)
    
    def update(self, payload, ID=None):
        """Updates local changes to the resource"""
        ID = ID or self.selected
        return self.client.request_json('PUT', self.ext + '/' + str(ID), payload)
            
    def delete(self, ID):
        """Deletes the resource"""
        ID = ID or self.selected
        return self.client.request_json('DELETE', self.ext + '/' + str(ID))
              
class Time(Resource):
    """Time of server"""

    ext = '/time'

class Coupons(Resource):
    """JSON Coupons"""
    
    
    ext = "/coupons"

        
class Products(Resource):
    """The collection of products in a store"""
   
    ext = '/products'


class Brands(Resource):
    """Brands collection"""

    ext = '/brands'


class Customers(Resource):
    """Customers collection"""

    ext = '/customers'


class Orders(Resource):
    """Orders collection"""

    ext = '/orders'
    

class OptionSets(Resource):
    """Option sets collection"""

    ext = '/optionsets'


class Categories(Resource):
    """Categories collection"""

    ext = '/categories'


class RequestException(RuntimeError):
    """There was an ambiguous exception that occurred while handling your
    request."""
    
    
class MissingStoreAddress(RequestException, ValueError):
    """The URL for a store must be provided"""
   
    
class MissingCredentials(RequestException, ValueError):
    """Authentication must be provided"""