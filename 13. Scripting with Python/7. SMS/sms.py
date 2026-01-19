from twilio.rest import Client

account_sid = "ACd1428chsdkjchkjc386789ghc6b3a8d093f71f4ec72eb9143e1f"
auth_token = "ad3a486ed06500c654d82028e56dcdsicp4709u334df"

client = Client(account_sid, auth_token)

message = client.messages.create(
    # media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
    from_="whatsapp:+14155238886",
    body="Hello . This is your bot: JARVIS, reporting on duty!",
    to="whatsapp:+918819982323",
)

print(message.sid)
