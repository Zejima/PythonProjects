import os
import twilio
import twilio.rest
from twilio.rest import Client

account_sid ="ACb2f4f8868779346457733a04736f69dc"
auth_token = "5544a416197d9d622eb72683eff4da99"

client = Client(account_sid, auth_token)

client.messages.create(
    to = "+17818505870",
    from_= "+17813949573",
    body = "This is a Twilio"

)

