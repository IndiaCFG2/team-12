from twilio.rest import Client
import smtplib
account_sid = "ACe2f10ba80d6f106f80c24a963ba04509"
auth_token = "aea579ac995ddb4615cf1746ddbe563a"
message = """
    Hello Student
    This is the content that will covered today,
    hope you are doing well.
    Youtube link: https://www.youtube.com/watch?v=C99rqP-lMjM \n
    It teaches life leasons
    """
def whatsapp():
    

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:918185039662'
    
    client.messages.create(body=message,from_=from_whatsapp_number,to=to_whatsapp_number)

def sms():
    # account_sid = "ACe2f10ba80d6f106f80c24a963ba04509"
    # auth_token = "aea579ac995ddb4615cf1746ddbe563a"
    # ​
    client = Client(account_sid, auth_token)
    client.messages.create(
    to="+919426158031",
    from_="+12565634331",
    body=message) 

def mail():
    message = """
    Hello Student
    This is the content that will covered today,
    hope you are doing well.
    Youtube link: https://www.youtube.com/watch?v=C99rqP-lMjM \n
    It teaches life leasons
    """
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("no.reply.hms.hms@gmail.com", "noreplyhms@1")
    smtpObj.sendmail("no.reply.hms.hms@gmail.com", "rohitdandamudi.1100@gmail.com", message)         
    print ("Successfully sent email")
    smtpObj.quit()