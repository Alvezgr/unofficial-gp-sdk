# Unofficial Geopagos APPS (Getnet, Viumi...) Python SDK 

This sdk provides basic methos to integrate geopagos apps (Getnet, Viumi, OpenPay, Taca Taca, Toque, Sipago, Uala Bis) payment API for a platform to start receiving payments.

## Requirements

python3
requests


## Installation 

Run ```git clone git@github.com:Alvezgr/unofficial-gp-sdk.git```

## Getting Started
Before you begin, you must request the API credential from your supplier (Getnet, Viumi, OpenPay, Taca Taca, Toque, Sipago, Uala Bis)

Request the your `Access Token` to the [geopagos auth](https://auth.geopagos.com/oauth/token) and API url

### Simple usage
  
```python
import geopagos

sdk = geopagos.SDK("ACCESS_TOKEN", "https://api.url.com")

urls = {
    "success": "https://www.mitienda.com/success",
    "failed": "https://www.mitienda.com/failed"
}

shipping =  {
    "name": "Correo Argentino",
    "price": {
        "currency": "032",
        "amount": 450
  }
}
items =  [
  {
      "name": "Lomo con papas",
      "unitPrice": {
          "currency": "032",
          "amount": 10050
      },
      "quantity": 2
  },
]

external_data = "25993"

result = sdk.order().create(
      items,
      urls=urls,
      shipping=shipping,
      external_data=external_data
)
payment = result["response"]

print(payment)
```
## Documentation 

Visit apps site for docs:
 - [Getnet](https://developers-sdk-documentation-site-santander.preprod.geopagos.com/)
 - [Viumi](https://developers.viumi.com.ar/)

Check our official code reference to explore all available functionalities.

## Tests
Ensure to define 
```bash
export ACCESS_TOKEN=access_token
export INVALID_ACCESS_TOKEN=invalid_token
export ORDER_ID=and_order_uuid
export API_URL=your_provider_url

```
```bash
pytest tests/
```

## Contributing

All contributions are welcome.

