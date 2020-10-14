#do make sure that imap is enabled in the respective email's settings
#Less secure apps also may have to be enabled
import imaplib
import email
import getpass
from email.header import decode_header
import numpy as np
import re
regex=re.compile('.*Thank you for applying.*')
pattern_uid = re.compile('\d+ \(UID (?P<uid>\d+)\)')
print("Enter email id")
username=input()
password=getpass.getpass("Enter password")
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
status, messages = imap.select("INBOX")
messages=int(messages[0])
print("The number of messages in your inbox are:{}".format(messages))
#The number of mails to scan for ,I'm setting it to 150 this can be edited to change number of messages to filter from
n=150
imap.create('JOBS')
for i in range(messages,messages-n,-1):
    res,msg=imap.fetch(str(i),"(RFC822)")
    for response in msg:
        if isinstance(response,tuple):
            msg=email.message_from_bytes(response[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            if regex.match(subject) is not None:
                print(regex.match(subject).group())
                print('='*100)
                resp,data=imap.fetch(str(i),'(UID)')
                msg_uid=pattern_uid.match(data[0].decode()).group('uid')
                result=imap.uid('COPY',msg_uid,'JOBS')
                if result[0]=='OK':
                    mov,data=imap.uid('STORE',msg_uid,'+FLAGS','(\Deleted)')
                    imap.expunge()
            else:
                continue
imap.logout()
