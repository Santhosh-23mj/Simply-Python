#!/usr/bin/python3

"""
A simple port scanner that uses TCP Connect Scan
"""

# Module 2 - Connecting to Target
from socket import *

services = {'21':'FTP','22':'SSH','25':'SMTP','80':'HTTP','443':'HTTPS','110':'IMAP'}

def connScan(tgthost,tgtport):
    try:
        conn = socket(AF_INET,SOCK_STREAM)
        conn.connect((tgthost,tgtport))
        if(str(tgtport) in services ):
            serv = services[str(tgtport)]
        else:
            serv = "Unknown"
        print("    [+] "+str(tgtport)+"\TCP OPEN "+serv)
        conn.close()
    except:
        print("    [+] "+str(tgtport)+"\TCP CLOSED "+serv)
        
        
            
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
        print("  [*] Scanning port "+str(port))
        connScan(tgthost,int(port))
        
