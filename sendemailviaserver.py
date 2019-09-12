import smtplib

s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com',587)
s.starttls()
s.login('AKIAVUSM25BOEJIC7MR4','BOK++0tDpJbzJ/S7uldPzxdPnwoNFBj/mF3447qfSsec')
msg= 'From: cretube53@gmail.com\nTo: cpejiofor@gmail.com\nSubject: Test email\n\n This is a test message'
s.sendmail('cretube53@gmail.com','cpejiofor@gmail.com', msg)