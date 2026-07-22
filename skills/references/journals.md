# Journals (`greenAPI.journals`)

Class: `Journals` in `tools/journals.py`.  
Index: https://green-api.com/en/docs/api/journals/

| Method | Params | Docs |
| --- | --- | --- |
| `getChatHistory` | `chatId`, optional `count` | https://green-api.com/en/docs/api/journals/GetChatHistory/ |
| `getMessage` | `chatId`, `idMessage` | https://green-api.com/en/docs/api/journals/GetMessage/ |
| `lastIncomingMessages` | optional `minutes` | https://green-api.com/en/docs/api/journals/LastIncomingMessages/ |
| `lastOutgoingMessages` | optional `minutes` | https://green-api.com/en/docs/api/journals/LastOutgoingMessages/ |
| `lastIncomingCalls` | optional `minutes` | https://green-api.com/en/docs/api/journals/LastIncomingCalls/ |
| `lastOutgoingCalls` | optional `minutes` | https://green-api.com/en/docs/api/journals/LastOutgoingCalls/ |

```python
history = greenAPI.journals.getChatHistory("79876543210@c.us", count=50)
msg = greenAPI.journals.getMessage("79876543210@c.us", id_message)
incoming = greenAPI.journals.lastIncomingMessages(minutes=1440)
```

Use `getMessage` to verify a message exists before quoting (`quotedMessageId`).
All methods have `*Async` variants.
