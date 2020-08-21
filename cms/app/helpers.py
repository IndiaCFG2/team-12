from twilio.rest import Client
import smtplib
account_sid = "" #twilio-acc-sid 
auth_token = "" #twilio-acc-auth-token
message = """
    Hello Student
    This is the content that will covered today,
    hope you are doing well.
    Youtube link:  \n
    It teaches life leasons
    """
def whatsapp():
    

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:'
    
    client.messages.create(body=message,from_=from_whatsapp_number,to=to_whatsapp_number)

def sms():
    client = Client(account_sid, auth_token)
    client.messages.create(
    to="", #twilio number
    from_="", #your phone number
    body=message) 

def mail():
    message = """
    Hello Student
    This is the content that will covered today,
    hope you are doing well.
    Youtube link: \n
    It teaches life leasons
    """
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("from_mail", "passwd")
    smtpObj.sendmail("from_mail", "to_mail", message)         
    print ("Successfully sent email")
    smtpObj.quit()