#!/usr/bin/python3

"""
A simple port scanner that uses TCP Connect Scan
"""

# Module 3 - Multi Threading
from socket import *
from threading import *
import string
import random

services = {'21':'FTP','22':'SSH','25':'SMTP','80':'HTTP','443':'HTTPS','110':'IMAP'}

Screenlock = Semaphore(value=1)
def connScan(tgthost,tgtport):
    try:
        conn = socket(AF_INET,SOCK_STREAM)
        conn.connect((tgthost,tgtport))
        conn.send(''.join(random.choices(list(string.ascii_letters),k=8)) + '\r\n')
        resp = conn.recv(1024)
        if(str(tgtport) in services ):
            serv = services[str(tgtport)]
        else:
            serv = "Unknown"
        Screenlock.acquire()    
        print("  [+] "+str(tgtport)+"\TCP OPEN "+serv)
        print("      [+] Banner : "+str(resp))
    except:
        Screenlock.acquire()
        print("  [-] "+str(tgtport)+"\TCP CLOSED "+serv)
    finally:
        Screenlock.release()
        conn.close()
        
            
def portScan(tgthost,tgtports):
    try:
        tgtIP = gethostbyname(tgthost)
    except:
        print("[-] Error : Couldn't resolve : "+tgthost+" : Host unknown")
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n[*] Scan Results for : "+tgtName[0])
    except:
        print("\n[*] Scan Results for : "+tgtIP)
    
    setdefaulttimeout(1)
    for port in tgtports:
        t = Thread(target=connScan,args=(tgthost,int(port)))
        t.start()
        
