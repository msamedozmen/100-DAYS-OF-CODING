import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC98a59cb71967516aaa0bcdf41d23cc61"
auth_token = "79c041398e3ddafbaf58373a272511eb"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12534652303",
  to="+905317435406"
)
print(message.sid)