# Q1. In this post we are disccuss about details in python how to send mail using python

import smtplib
import os

# Securely Load Credentials from environment variables
sender = os.getenv("technology@gmail.com")
password = os.getenv("TS@2025")

reciver  = "reciver@gmail.com"
subject = "Write Email Using Python"
body = "This email write by Shailesh Founder of TS_Group just for check it is workable or not. "

# header and body of email
#   
message = f""" from : Shailesh <{sender}>
                To: TechnologySecret<{reciver}>
                Subject: {subject} \n {body} 
"""



try:            #Conneted gamil to SMTP server
    server = smtplib.SMTP("smtp.gmail.com",587)   
    server.starttls()           #Upgrade to secure connection
    server.login(sender,password)
    print("Logged In Successful !")
    server.sendmail(sender, reciver, message)
    print("Email Has been sent Successfully")

except smtplib.SMTPAuthenticationError:
    print("Authentication Error: Unable to Login, Check your email and Password ")

except Exception as e:
    print(f"An Error Occuredd, please check your server : {e}")


