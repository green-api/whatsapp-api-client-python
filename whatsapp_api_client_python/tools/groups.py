from array import ArrayType, array
import os.path
from whatsapp_api_client_python.response import Response


class Groups:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def addGroupParticipant(self, 
            groupId: str, 
            participantChatId: str) -> Response:
            'The method adds a participant to a group chat.'

            requestBody = {
                'groupId': groupId,
                'participantChatId': participantChatId,
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/AddGroupParticipant/{{apiTokenInstance}}',
                requestBody)

    def createGroup(self, groupName: str, chatIds: array) -> Response:
            'The method is aimed for creating a group chat.'
            
            requestBody = {
                'groupName': groupName,
                'chatIds': chatIds
            }

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/CreateGroup/{{apiTokenInstance}}',
                requestBody)

    def getGroupData(self, groupId: str) -> Response:
            'The method gets group chat data.'

            requestBody = {
                'groupId': groupId
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetGroupData/{{apiTokenInstance}}',
                requestBody)

    def leaveGroup(self, groupId: str) -> Response:
            'The method makes the current account user leave the group chat.'

            requestBody = {
                'groupId': groupId
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/LeaveGroup/{{apiTokenInstance}}',
                requestBody)

    def removeAdmin(self, groupId: str, participantChatId: str) -> Response:
            'The method removes a participant from group chat '\
            'administartion rights.'

            requestBody = {
                'groupId': groupId,
                'participantChatId': participantChatId
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/RemoveAdmin/{{apiTokenInstance}}',
                requestBody)

    def removeGroupParticipant(self, 
        groupId: str, 
        participantChatId: str) -> Response:
            'The method removes a participant from a group chat.'

            requestBody = {
                'groupId': groupId,
                'participantChatId': participantChatId
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/RemoveGroupParticipant/{{apiTokenInstance}}',
                requestBody)

    def setGroupAdmin(self, 
        groupId: str, 
        participantChatId: str) -> Response:
            'The method sets a group chat participant as an administrator.'

            requestBody = {
                'groupId': groupId,
                'participantChatId': participantChatId
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetGroupAdmin/{{apiTokenInstance}}',
                requestBody)

    def setGroupPicture(self, 
        groupId: str, 
        path: str) -> Response:
            'The method sets a group picture.'

            requestBody = {
                'groupId': groupId
            }

            pathParts = os.path.split(path)
            file = pathParts[1]

            files = [
                ('file',(file, open(path,'rb'),'image/jpeg'))
            ]
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetGroupPicture/{{apiTokenInstance}}',
                requestBody, files)

    def updateGroupName(self, 
        groupId: str, 
        groupName: str) -> Response:
            'The method changes a group chat name.'

            requestBody = {
                'groupId': groupId,
                'groupName': groupName
            }
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/UpdateGroupName/{{apiTokenInstance}}',
                requestBody)