import imaplib
import smtplib
import email
import os
import time
import base64

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('pokegoloco@gmail.com', 'password')
mail.list()

def check_inbox():
	value = mail.select("inbox")[1]
	mail.close
	return value

def get_mail():
	mail.select("inbox")
	result, data = mail.search(None, 'UnSeen')
	ids = data[0]
	id_list = ids.split()
	latest_email_id = id_list[-1]
	result, data = mail.fetch(latest_email_id, "(RFC822)")
	raw_email = data[0][1]
	mail.store(latest_email_id,'+X-GM-LABELS','\\Trash')
	mail.close
	return raw_email

def go():
	raw_email = get_mail()
	msg = email.message_from_string(raw_email)
	address = msg['from']
	if '<' in address:
		y = address.split('<',1)[1]
		address = y.split('>')[0]
	if '+' in address:
		address = address[2:]
	print(address)

	try:
		gps = raw_email.split('?', 1)[1]
		z = gps.split('?')
		gps = z[0]
		print(gps)
		if ' ' in gps:
			start()
		s = "python main.py -u username -p password -l "+gps+" -m "+address
		os.system(s)
	except:
		message = "Incorrect Format, Try again"
		f = open("Output.txt", "w")
		f.write(message)
		f.close()
		print(message)
		s = "python SendText.py "+address
		os.system(s)

def wait():
	time.sleep(60)
	start()
	
def start():
	value = check_inbox()
	if value[0] == '0':
		print("waiting")
		wait()
	else:
		print("going")
		go()

start()





