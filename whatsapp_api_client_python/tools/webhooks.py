class Webhooks:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        self.started = False

    def startReceivingNotifications(self, onEvent) -> bool:
        self.started = True
        self.job(onEvent)

    def stopReceivingNotifications(self) -> bool:
        self.started = False

    
    def job(self, onEvent) -> None:
        print('Incoming notifications are being received. '\
        'To interrupt, press Ctrl+C')
        try:
            while self.started == True:
                resultReceive = self.restApi.receiving.receiveNotification()
                if resultReceive.code == 200:
                    if resultReceive.data == None:
                        # There are no incoming notifications, 
                        # we send the request again
                        continue
                    body = resultReceive.data['body']
                    typeWebhook = body['typeWebhook']
                    onEvent(typeWebhook, body)    
                    self.restApi.receiving.deleteNotification(
                        resultReceive.data['receiptId'])
            print('End receiving')
        except KeyboardInterrupt:
            print('End receiving')
            pass