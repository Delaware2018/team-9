from twilio.rest import Client
import requests

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC096f8dc0f193bfee6c2faa3e93e0198e'
auth_token = '3dfb99b0d9ce70ba3a10c76eeb64026b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello from BE POSITIVE, would you like to match your original donation to continue combating childhood cancer?",
                     from_='+16468591385',
                     to='+16465888148'
                 )

print(message.sid)
