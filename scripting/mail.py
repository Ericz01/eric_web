import smtplib

smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()# Make a server connection
smtObj.starttls()# Initiate tls mode
smtObj.login('ericzerico01@gmail.com', 'some_password')
smtObj.sendmail('ericzerico01@gmail.com', 'erickinyua770@gmail.com', 'Subject: Hello. \n Hey, just checking this new Python way of sending mails😎')
smtObj.quit()