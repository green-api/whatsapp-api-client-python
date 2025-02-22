from whatsapp_api_client_python import API

greenAPI = API.GreenApiPartner(
    "gac.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
)


def main():
    response = greenAPI.partner.getInstances()
    print(response.data)

if __name__ == '__main__':
    main()
