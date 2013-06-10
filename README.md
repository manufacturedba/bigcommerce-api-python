BigCommerce API V2 - Python Client
==================================

Original Credit: 

* Project: [Bigcommerce](https://github.com/bigcommerce/bigcommerce-api-python/ "Bigcommerce authored library")

> This module provides an object-oriented wrapper around the BigCommerce V2 API for use in Python projects or via the Python shell.
>
>Requirements:
>
>- Python 2.3+
>- requests
>
>A valid API key is required to authenticate requests. To grant API access for user, go to Control Panel > Users > Edit User and make sure that the 'Enable the XML API?' checkbox is ticked.

>Usage:

```
#!/usr/bin/python
import bigcommerce.api as api

api.Connection.host = 'store.mybigcommerce.com'
api.Connection.user = 'admin'
api.Connection.api_key = '22d05a34ecb25e2d95f5e0208d129b5e1668cade'

coupons = api.Coupons().get({'code':'10%OFF')

coupon = api.Coupons().get_by_id(38)
coupon.code = "20%ISAY"
coupon.update()

coupon = api.Coupons().create(JSONPAYLOAD)
coupon.get_json()

```

