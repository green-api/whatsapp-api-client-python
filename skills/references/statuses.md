# Statuses (`greenAPI.statuses`)

Class: `Statuses` in `tools/statuses.py`.  
Index: https://green-api.com/en/docs/api/statuses/ (β-version in docs)

| Method | Params | Docs |
| --- | --- | --- |
| `sendTextStatus` | `message`, optional `backgroundColor`, `font`, `participants` | https://green-api.com/en/docs/api/statuses/SendTextStatus/ |
| `sendVoiceStatus` | `urlFile`, `fileName`, optional `backgroundColor`, `participants` | https://green-api.com/en/docs/api/statuses/SendVoiceStatus/ |
| `sendMediaStatus` | `urlFile`, `fileName`, optional `caption`, `participants` | https://green-api.com/en/docs/api/statuses/SendMediaStatus/ |
| `deleteStatus` | `idMessage` | https://green-api.com/en/docs/api/statuses/DeleteStatus/ |
| `getStatusStatistic` | `idMessage` | https://green-api.com/en/docs/api/statuses/GetStatusStatistic/ |
| `getIncomingStatuses` | optional `minutes` | https://green-api.com/en/docs/api/statuses/GetIncomingStatuses/ |
| `getOutgoingStatuses` | optional `minutes` | https://green-api.com/en/docs/api/statuses/GetOutgoingStatuses/ |

```python
greenAPI.statuses.sendTextStatus("Hello status")
greenAPI.statuses.getOutgoingStatuses(minutes=1440)
```

All have `*Async` variants. Confirm parameter enums (fonts, colors) on the official page
before hardcoding values.
