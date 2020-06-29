from twilio.rest import Client

account_sid = 'ACbfc5d3772f243f4c03f08e73748cb1c6'
auth_token = 'a35f3c5a94cee4490d618fa8273d0dee'
client = Client(account_sid, auth_token)

def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='hello world ',
        to='whatsapp:+27717863496'
    )

    print(message.sid)