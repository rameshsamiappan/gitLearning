from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7b413c4720fe51b591c0dc37103c361f"
auth_token  = "7d3b558d1aba5afaa225d80b5cee8fc5"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hey, Ramesh",
    to="+919841364548",    # Replace with your phone number
    from_="+12249002745") # Replace with your Twilio number
print message.sid
