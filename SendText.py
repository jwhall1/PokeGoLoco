import smtplib
import sys
import os

# Credentials (if needed)
# I recomend you create a new email account just for this
username = 'pokegoloco'
password = 'password'
fromaddr = 'pokegoloco@gmail.com'
toaddrs  = sys.argv[1]
f = open("Output.txt", "r")
msg = f.read()
if len(msg) < 10:
	msg = "No monsters around!"
f.close
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
os.system("python PokeGoLoco.py")



