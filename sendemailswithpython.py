import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email='cpejiofor@gmail.com'
password = ''
send_to_email ='jdeguglielmo@umass.edu'
subject ='Go Here'
message = 'Go to Better Money Habits to get tips on how to manage your money'


msg = MIMEMultipart()
msg['From'] = email
msg['To']=send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls() 
server.login(email, password)
text = msg.as_string()
server.sendmail(email,send_to_email,text)
server.quit()
