from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.statuses.sendTextStatus(
    "I sent this status using Green Api Python SDK!", 
    "#54c774", 
    "NORICAN_REGULAR")

    print(response.data)

if __name__ == '__main__':
    main()
