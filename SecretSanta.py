"""
This requires that unsecured option be enabled in the senders gmail setting and also
the email was not reaching nikishah@in.ibm.com through this.
"""

import smtplib, ssl


port = 465  # For SSL
sender_email = "secretsantaniki20@gmail.com"
receiver_email = "nikitashahu@gmail.com"
message = """\
Subject: Hi there! Lets spread some christmas cheer !!! :) 


You are the secret santa for XYZ. :) :) 

Please send a gift upto INR 500 to XYZ currently residing at
ABC.

Please ensure that the gift reaches XYZ by 15th Dec.

Details about virtual gift unwrapping will soon be sent ! 

Disclaimer: This message is sent from a Python script. 
Do not reply to this, incase of suggestions or queries, please 
reach out at 7411414721 
or nikishah@in.ibm.com 
or slack -> nikishah

"""

password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

#with here is used in place of try/finally
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("secretsantaniki20@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
