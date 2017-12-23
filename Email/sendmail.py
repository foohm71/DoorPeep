#!/usr/bin/env python

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['me@gmail.com','you@yahoo.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "[DoorPeep] Camera Started" 
msg['From'] = 'myemail@gmail.com'
msg['Reply-to'] = 'myemail@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("URL for Camera is %s" % str(sys.argv[1]))
msg.attach(part)
 
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("myemail@gmail.com", "password")
 
server.sendmail(msg['From'], emaillist , msg.as_string())


