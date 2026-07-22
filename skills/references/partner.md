# Partner API (`GreenApiPartner`)

Class: `Partner` in `tools/partner.py`, attached only to `API.GreenApiPartner`.  
Docs base: https://green-api.com/en/docs/partners/

```python
from whatsapp_api_client_python import API

partner = API.GreenApiPartner(partnerToken="YOUR_PARTNER_TOKEN")
```

| Method | Params | Docs |
| --- | --- | --- |
| `getInstances` | — | https://green-api.com/en/docs/partners/getInstances/ |
| `createInstance` | `requestBody: Dict` | https://green-api.com/en/docs/partners/createInstance/ |
| `deleteInstanceAccount` | `idInstance: int` | https://green-api.com/en/docs/partners/deleteInstanceAccount/ |

```python
instances = partner.partner.getInstances()
created = partner.partner.createInstance({"...": "..."})  # fields per partner docs
partner.partner.deleteInstanceAccount(1101000001)
```

Do **not** call `greenAPI.partner` on a normal `GreenAPI` client — the attribute is not
created there.
