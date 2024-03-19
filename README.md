# Unofficial Geopagos APPS (Getnet, Viumi...) Python SDK 

This sdk provides basic methos to integrate geopagos apps (Getnet, Viumi, OpenPay, Taca Taca, Toque, Sipago, Uala Bis) payment API for a platform to start receiving payments.

## Requirements

Python 3 or higher.

## Installation 

Run ```git clone git@github.com:Alvezgr/unofficial-gp-sdk.git```

## Getting Started
Before you begin, you must request the API credential from your supplier (Getnet, Viumi, OpenPay, Taca Taca, Toque, Sipago, Uala Bis)

Request the your `Access Token` to the [geopagos auth](https://auth.geopagos.com/oauth/token)

### Simple usage
  
```python
import gp

sdk = gp.SDK("ACCESS_TOKEN")

order_data = {
  "data": {
    "attributes": {
      "redirect_urls": {
        "success": "https://www.mitienda.com/success",
        "failed": "https://www.mitienda.com/failed"
      },
      "shipping": {
        "name": "Correo Argentino",
        "price": {
          "currency": "032",
          "amount": 450
        }
      },
      "items": [
        {
          "name": "Lomo con papas",
          "unitPrice": {
            "currency": "032",
            "amount": 10050
          },
          "quantity": 2
        },
        {
          "unitPrice": {
            "currency": "032",
            "amount": 1
          },
          "quantity": 1
        }
      ],
      "externalData": "{\"NroLegajo\": 25993}"
    }
  }
}

result = sdk.order().create(order_data)
payment = result["response"]

print(payment)
```
## Documentation 

Visit apps site for docs:
 - [Getnet](https://www.mercadopago.com/developers/en/reference)
 - [Viumi](https://developers.viumi.com.ar/)

Check our official code reference to explore all available functionalities.

## Contributing

All contributions are welcome.

