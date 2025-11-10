from whatsapp_api_client_python import API

greenAPI = API.GreenApiPartner(
    "gac.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
)


def main():
    response = greenAPI.partner.deleteInstanceAccount(1103123456)
    print(response.data)

if __name__ == '__main__':
    main()
