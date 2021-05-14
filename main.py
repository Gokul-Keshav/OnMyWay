from web_server import app


if __name__ == '__main__':
    from twilio.rest import Client

    account_sid = 'ACb09992f4f01d23dce0ddc209c6a47520'
    auth_token = 'e4eb6df7df0bb737cefb647fcac805b2'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hi Boomila are you studying poility?',
        to='whatsapp:+918124992924'
    )

    print(message.sid)
