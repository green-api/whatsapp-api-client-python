# Marking (`greenAPI.marking`)

Class: `Marking` in `tools/marking.py`.

## `readChat`

Docs: https://green-api.com/en/docs/api/marks/ReadChat/

| Param | Required | Notes |
| --- | --- | --- |
| `chatId` | yes | |
| `idMessage` | no | if omitted, marks chat as read per API rules |

```python
greenAPI.marking.readChat("79876543210@c.us")
greenAPI.marking.readChat("79876543210@c.us", idMessage="3EB0...")
```

Async: `readChatAsync`.
