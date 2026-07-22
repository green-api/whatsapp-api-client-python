# Groups (`greenAPI.groups`)

Class: `Groups` in `tools/groups.py`.  
Index: https://green-api.com/en/docs/api/groups/

Group chat IDs end with `@g.us` and are **returned by the API** — do not invent them.
Docs: https://green-api.com/en/docs/api/chat-id/

## `createGroup`

Docs: https://green-api.com/en/docs/api/groups/CreateGroup/

| Param | Required | Notes |
| --- | --- | --- |
| `groupName` | yes | max 100 chars |
| `chatIds` | yes | list of participant `@c.us` ids |

Response: `created`, `chatId`, `groupInviteLink`.

**Rate:** create no more than ~1 group per 5 minutes. Numbers without WhatsApp can cause
errors or risk blocks.

```python
r = greenAPI.groups.createGroup("My group", ["79876543210@c.us"])
group_id = r.data["chatId"]
```

## Other methods

| Method | Required params | Docs |
| --- | --- | --- |
| `updateGroupName` | `groupId`, `groupName` | https://green-api.com/en/docs/api/groups/UpdateGroupName/ |
| `getGroupData` | `groupId` | https://green-api.com/en/docs/api/groups/GetGroupData/ |
| `addGroupParticipant` | `groupId`, `participantChatId` | https://green-api.com/en/docs/api/groups/AddGroupParticipant/ |
| `removeGroupParticipant` | `groupId`, `participantChatId` | https://green-api.com/en/docs/api/groups/RemoveGroupParticipant/ |
| `setGroupAdmin` | `groupId`, `participantChatId` | https://green-api.com/en/docs/api/groups/SetGroupAdmin/ |
| `removeAdmin` | `groupId`, `participantChatId` | https://green-api.com/en/docs/api/groups/RemoveAdmin/ |
| `setGroupPicture` | `groupId`, `path` (local file) | https://green-api.com/en/docs/api/groups/SetGroupPicture/ |
| `leaveGroup` | `groupId` | https://green-api.com/en/docs/api/groups/LeaveGroup/ |
| `updateGroupSettings` | `groupId`, optional booleans `allowParticipantsEditGroupSettings`, `allowParticipantsSendMessages` | https://green-api.com/en/docs/api/groups/UpdateGroupSettings/ |

All methods have `*Async` variants.
