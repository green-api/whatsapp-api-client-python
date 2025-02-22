from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.statuses.getIncomingStatuses(1400) # minutes argument is Optional 
    print(response.data)

    response = greenAPI.statuses.getOutgoingStatuses(1400) # minutes argument is Optional
    print(response.data)

    response = greenAPI.statuses.getStatusStatistic('BAE54F518532FCB1')
    print(response.data)

if __name__ == '__main__':
    main()
