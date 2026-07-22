# Queues (`greenAPI.queues`)

Class: `Queues` in `tools/queues.py`.  
Index: https://green-api.com/en/docs/api/queues/

| Method | HTTP (SDK) | Docs |
| --- | --- | --- |
| `showMessagesQueue` | GET | https://green-api.com/en/docs/api/queues/ShowMessagesQueue/ |
| `clearMessagesQueue` | GET | https://green-api.com/en/docs/api/queues/ClearMessagesQueue/ |
| `getMessagesCount` | GET | https://green-api.com/en/docs/api/queues/GetMessagesCount/ |
| `getWebhooksCount` | GET | https://green-api.com/en/docs/api/queues/GetWebhooksCount/ |
| `clearWebhooksQueue` | DELETE | https://green-api.com/en/docs/api/queues/ClearWebhooksQueue/ |

No request body parameters. All have `*Async` variants.

Outgoing messages sit in the send queue until sent (delay setting applies).
Incoming notifications sit in the webhook queue until deleted / delivered.
