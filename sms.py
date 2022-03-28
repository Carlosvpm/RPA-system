from contextlib import nullcontext
import environments
from twilio.rest import Client

sms_sent = False


def send_sms(message):
    global sms_sent
    account_sid = environments.TWILIO_ACCOUNT_SID
    auth_token = environments.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    if sms_sent:
        return print('Já foi notificado!')
    else:
        sms_sent = True
        return client.messages.create(from_=(environments.TWILIO_PHONE_NUMBER),
                                  to=(environments.CELL_PHONE_NUMBER),
                                  body=message)
