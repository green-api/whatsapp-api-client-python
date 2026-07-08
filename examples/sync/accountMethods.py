from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # Get last 50 state changes
    response = greenAPI.account.getStateInstanceHistory(count=50)
    print(response.data)

    # Get full history (default 100 records)
    response = greenAPI.account.getStateInstanceHistory()
    print(response.data)

    # Refresh API token (beta). The old token becomes invalid after this call.
    response = greenAPI.account.updateApiToken()
    print(response.data)


if __name__ == '__main__':
    main()
