#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8').encode(), addr)

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send to itabas...', 'plain', 'utf-8')
msg['From'] = _format_addr('<%s>' % from_addr)
msg['To'] = _format_addr('<%s>' % to_addr)
msg['Subject'] = Header('Test python SMTP', 'utf-8').encode()
msg.attach(MIMEText)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()