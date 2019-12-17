from twilio.rest import Client



account_sid = 'ACf72d08db3e903a8b1c7cef4abcefd1ed'
auth_token = 'a6373d036f80a7ccbfc32fd173883a2b'
client = Client(account_sid, auth_token)
message = client.messages.create(from_='+19386669137',body ='hello ',to ="+918919538130",)

print(message.sid)
