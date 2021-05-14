from . import app
from flask import request, render_template

DEBUG = True


def print_d(line):
    if DEBUG:
        print(line)


@app.route('/')
def play_content():
    return render_template('index.html')


@app.route('/alert', methods=['POST'])
def send_alert():
    print(request.get_json())
    data = request.get_json()
    from twilio.rest import Client

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"Trip Request:\n"
             f"Name: {data['name']}\n"
             f"Phone: {data['phone']}\n"
             f"Present Location: {data['location']}\n"
             f"Destination: {data['destination']}\n"
             f"Passengers Count: {data['passengers']}\n"
             f"Date: {data['date']}",
        to='whatsapp:+91'
    )
    print(message.sid)
    return "Success"
