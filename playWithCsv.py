import csv
import random

emailMsg = """\
Hi {gifter} !  

You are chose to be the secret santa for {giftee}. :) :) 

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

with open("secretSantaTest.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    allNames = []
    allDetails ={}
    giftsdonefor = []

    for name, email, phone, address in reader:
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
        giftee = random.choice(possiblechoices)
        newEmailMsg = emailMsg.format(gifter=gifter, giftee=giftee, address=allDetails.get(giftee)['address'],
                                      phone=allDetails.get(giftee)['address'])
        print(newEmailMsg)
        print(gifter+'  '+giftee)
        giftsdonefor.append(giftee)

