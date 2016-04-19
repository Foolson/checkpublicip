import requests, smtplib
from email.mime.text import MIMEText
url = 'http://myexternalip.com/raw'
r = requests.get(url)
newIp = str(r.text).rstrip()
print('* New public IP from myexternalip.com: '+newIp)
print('* Trying to create new IP-log')
try:
  f = open('ip-log', 'x')
  f.write('0.0.0.0')
  f.close()
except FileExistsError:
  print('* IP-log already exists!')
f = open('ip-log', 'r')
oldIp = f.read()
f.close()
print('* Reading old public IP from IP-log: '+oldIp)
print('* Comparing old public IP and new public IP')
if newIp != oldIp:
  print('* New public IP detected, writing to IP-log')
  f = open('ip-log','w')
  f.write(newIp)
  f.close()
  print('* Sending e-mail with new public IP')
  msg = MIMEText('New public IP-address: '+newIp)
  msg['Subject'] = 'New public IP!'
  msg['From'] = 'noreply@localhost.localdomain'
  msg['To'] = 'DIN MAIL'
  s = smtplib.SMTP('mailout.comhem.se')
  s.send_message(msg)
  s.quit()
print('* No new public IP')
