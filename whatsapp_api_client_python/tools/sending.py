from array import array
import os.path
from whatsapp_api_client_python.response import Response


class Sending:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def sendButtons(self, chatId: str, message: str, footer: str,
                    buttons: array, quotedMessageId: str = None, 
                    archiveChat: bool = None) -> Response:
            'The method is aimed for sending a button message to a personal '\
            'or a group chat. The message will be added to the send queue. '\
            'Checking whatsapp authorization on the phone (i.e. availability '\
            'in linked devices) is not performed. The message will be kept '\
            'for 24 hours in the queue and will be sent immediately after '\
            'phone authorization. The rate at which messages are sent from '\
            'the queue is managed by Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'message': message,
                'footer': footer,
                'buttons': buttons,
            }

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId
            if archiveChat != None:
                requestBody['archiveChat'] = archiveChat

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendButtons/{{apiTokenInstance}}',
                requestBody)

    def sendContact(self, chatId: str, contact: object,
                    quotedMessageId: str = None) -> Response:
            'The method is aimed for sending a contact message. '\
            'Contact visit card is created and sent to a chat. '\
            'The message will be added to the send queue. '\
            'Linked device not required when sending. '\
            'Messages will be kept for 24 hours in the queue until account '\
            'will be authorized The rate at which messages are sent from '\
            'the queue is managed by Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'contact': contact
            }

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendContact/{{apiTokenInstance}}',
                requestBody)

    def sendFileByUpload(self, chatId: str, path: str,
                    fileName: str = None,
                    caption: str = None,
                    quotedMessageId: str = None) -> Response:
            'The method is aimed for sending a file uploaded by form '\
            '(form-data). The message will be added to the send queue. '\
            'The rate at which messages are sent from the queue is managed '\
            'by Message sending delay parameter.'\
            'Video, audio and image files available for viewing and listening '\
            'to are sent as in native-mode WhatsApp. Documents are sent in '\
            'the same way as in native-mode WhatsApp. Outgoing file type and '\
            'send method is determined by the file extension. '\
            'Description is only added to images and video.'\
            'The maximum size of outgoing files is 37 MB.'

            pathParts = os.path.split(path)
            if fileName == None:
                fileName = pathParts[1]

            files = [
                ('file', open(path,'rb'))
            ]

            requestBody = {
                'chatId': chatId,
                'fileName': fileName
            }

            if caption != None:
                requestBody['caption'] = caption

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendFileByUpload/{{apiTokenInstance}}',
                requestBody, files)

    def sendFileByUrl(self, chatId: str, urlFile: str,
                    fileName: str = None,
                    caption: str = None,
                    quotedMessageId: str = None,
                    archiveChat: bool = None) -> Response:
            'The method is aimed for sending a file uploaded by Url '\
            'The message will be added to the send queue. '\
            'The rate at which messages are sent from the queue is managed '\
            'by Message sending delay parameter.'\
            'Video, audio and image files available for viewing and listening '\
            'to are sent as in native-mode WhatsApp. Documents are sent in '\
            'the same way as in native-mode WhatsApp. Outgoing file type and '\
            'send method is determined by the file extension. '\
            'Description is only added to images and video.'\
            'The maximum size of outgoing files is 37 MB.'

            requestBody = {
                'chatId': chatId,
                'urlFile': urlFile,
                'fileName': fileName
            }

            if caption != None:
                requestBody['caption'] = caption

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId

            if archiveChat != None:
                requestBody['archiveChat'] = archiveChat

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendFileByUrl/{{apiTokenInstance}}',
                requestBody)

    def sendLink(self, chatId: str, urlLink: str,
                    quotedMessageId: str = None) -> Response:
            'The method is aimed for sending a message with a link, by which '\
            'an image preview, title and description will be added. '\
            'Linked device not required when sending. Messages will be kept '\
            'for 24 hours in the queue until account will be authorized '\
            'Image, title and description are obtained from Open Graph page '\
            'template being linked to. The message will be added to the send '\
            'queue. The rate at which messages are sent from the queue is '\
            'managed by Messages sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'urlLink': urlLink
            }

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendLink/{{apiTokenInstance}}',
                requestBody)

    def sendListMessage(self, chatId: str, message: str, sections: array,
                    title: str = None,
                    footer: str = None,
                    buttonText: str = None,
                    quotedMessageId: str = None,
                    archiveChat: str = None) -> Response:
            'The method is aimed for sending a message with a select button '\
            'from a list of values to a personal or a group chat. '\
            'The message will be added to the send queue. Checking whatsapp '\
            'authorization on the phone (i.e. availability in linked devices) '\
            'is not performed. The message will be kept for 24 hours in the '\
            'queue and will be sent immediately after phone authorization. '\
            'The rate at which messages are sent from the queue is managed by '\
            'Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'message': message,
                'sections': sections
            }

            if title != None:
                requestBody['title'] = title
            if footer != None:
                requestBody['footer'] = footer
            if buttonText != None:
                requestBody['buttonText'] = buttonText
            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId 
            if archiveChat != None:
                requestBody['archiveChat'] = archiveChat

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendListMessage/{{apiTokenInstance}}',
                requestBody)

    def sendLocation(self, chatId: str, latitude: float, longitude: float,
                    nameLocation: str = None,
                    address: str = None,
                    quotedMessageId: str = None) -> Response:
            'The method is aimed for sending location message. The message '\
            'will be added to the send queue. Linked device not required '\
            'when sending. Messages will be kept for 24 hours in the queue '\
            'until account will be authorized The rate at which messages are '\
            'sent from the queue is managed by Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'latitude': latitude,
                'longitude': longitude
            }

            if nameLocation != None:
                requestBody['nameLocation'] = nameLocation
            if address != None:
                requestBody['address'] = address
            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId 

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendLocation/{{apiTokenInstance}}',
                requestBody)

    def sendMessage(self, chatId: str, message: str,
                    quotedMessageId: str = None,
                    archiveChat: str = None) -> Response:
            'The method is aimed for sending a text message to a personal or '\
            'a group chat. The message will be added to the send queue. '\
            'Linked device not required when sending. Messages will be kept '\
            'for 24 hours in the queue until account will be authorized '\
            'The rate at which messages are sent from the queue is managed '\
            'by Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'message': message
            }

            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId
            if archiveChat != None:
                requestBody['archiveChat'] = archiveChat 

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendMessage/{{apiTokenInstance}}',
                requestBody)

    def sendTemplateButtons(self, chatId: str, message: str,
                    templateButtons: array,
                    footer: str = None,
                    quotedMessageId: str = None,
                    archiveChat: str = None) -> Response:
            'The method is aimed for sending a message with template list '\
            'interacrive buttons to a personal or a group chat. The message '\
            'will be added to the send queue. Checking whatsapp authorization '\
            'on the phone (i.e. availability in linked devices) '\
            'is not performed. The message will be kept for 24 hours in the '\
            'queue and will be sent immediately after phone authorization. '\
            'The rate at which messages are sent from the queue is managed '\
            'by Message sending delay parameter.'

            requestBody = {
                'chatId': chatId,
                'message': message,
                'templateButtons': templateButtons
            }

            if footer != None:
                requestBody['footer'] = footer
            if quotedMessageId != None:
                requestBody['quotedMessageId'] = quotedMessageId
            if archiveChat != None:
                requestBody['archiveChat'] = archiveChat 

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SendTemplateButtons/{{apiTokenInstance}}',
                requestBody)