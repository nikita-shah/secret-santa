from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import random

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = """\
Hi {gifter} !  

You are chosen to be the secret santa for {giftee}. :) :) 

Please send a gift upto INR 500 to {giftee} currently residing at
{address} with phone number {phone}.

Please ensure that the gift reaches {giftee} by 15th Dec.

Details about virtual gift unwrapping will soon be sent ! 

Incase of suggestions or queries, 
please reach out to 7411414721 
or nikishah@in.ibm.com 
or slack -> nikishah
Nikita Shah
"""

with open("secret-santa-contact-details.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    allNames = []
    allDetails ={}
    giftsdonefor = []
    secretSantaChoices = {}

    for name, email, address, phone in reader:
        allNames.append(name)
        allDetails[name] = {'email':email,'phone':phone,'address':address}


    for gifter in allNames:
        possiblechoices = allNames.copy()
        if gifter in possiblechoices:
            possiblechoices.remove(gifter)
        if len(giftsdonefor) > 0:
                for giftdonefor in giftsdonefor:
                 if giftdonefor in possiblechoices :
                  possiblechoices.remove(giftdonefor)
        try:
            giftee = random.choice(possiblechoices)
            giftsdonefor.append(giftee)
            secretSantaChoices[gifter]={'giftee':giftee}
        except:
            print('Please retry as the random choice did not come out well !')
            exit()

    for gifter in secretSantaChoices:
        giftee = secretSantaChoices.get(gifter)['giftee']
        newEmailMsg = emailMsg.format(gifter=gifter, giftee=giftee, address=allDetails.get(giftee)['address'],
                                      phone=allDetails.get(giftee)['phone'])
        print('Sending email to '+gifter)
        giftsdonefor.append(giftee)
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = allDetails.get(gifter)['email']
        mimeMessage['subject'] = 'Secret Santa invitation : Lets spread some christmas cheer !!! :)'
        mimeMessage.attach(MIMEText(newEmailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print(message)


