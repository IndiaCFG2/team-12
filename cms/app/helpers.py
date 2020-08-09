from twilio.rest import Client

def whatsapp():
    account_sid = "ACe2f10ba80d6f106f80c24a963ba04509"
    auth_token = "aea579ac995ddb4615cf1746ddbe563a"

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:919426165580'

    client.messages.create(body='Ahoy, world!',from_=from_whatsapp_number,to=to_whatsapp_number)