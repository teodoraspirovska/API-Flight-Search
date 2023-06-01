from twilio.rest import Client
import os

twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
twilio_verified_number = os.environ.get("TWILIO_VERIFIED_NUMBER")


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_sid, twilio_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_virtual_number,
            to=twilio_verified_number,
        )

        print(message.sid)
