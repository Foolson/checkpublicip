import requests, smtplib
from email.mime.text import MIMEText  
newIp = requests.get('http://myexternalip.com/raw').text.rstrip()
try:
  f = open('ip-log', 'x')
  f.write('0.0.0.0')
  f.close()
except FileExistsError:
  pass
f = open('ip-log', 'r')
oldIp = f.read()
f.close()
if newIp != oldIp:
  f = open('ip-log','w')
  f.write(newIp)
  f.close()
  msg = MIMEText('New public IP-address: '+newIp)
  msg['Subject'] = 'New public IP!'
  msg['From'] = 'noreply@localhost.localdomain'
  msg['To'] = 'DIN MAIL'
  s = smtplib.SMTP('mailout.comhem.se')
  s.send_message(msg)
  s.quit()
