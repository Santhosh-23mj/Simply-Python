#!/usr/bin/python3

"""
A simple port scanner that uses TCP Connect Scan
"""

# Final Program - A simple portscanner
import optparse
from socket import *
from threading import *
import string
import random
import sys

Screenlock = Semaphore(value=1)
def connScan(tgthost,tgtport):
    try:
        conn = socket(AF_INET,SOCK_STREAM)
        conn.connect((tgthost,tgtport))
        payload = ''.join(random.choices(list(string.ascii_letters),k=8)) + '\r\n'
        payload = bytes(payload,'utf-8')
        conn.send(payload)
        resp = (conn.recv(1024)).decode()
        Screenlock.acquire()    
        print("[+] "+str(tgtport)+"\TCP OPEN ")
        print("[+] Banner : ")
        print(str(resp))
    except:
        Screenlock.acquire()
        print("[-] "+str(tgtport)+"\TCP CLOSED ")
    finally:
        Screenlock.release()
        conn.close()
        
            
def portScan(tgthost,tgtports):
    try:
        tgtIP = gethostbyname(tgthost)
        print("[+] Scan Results for : "+tgtIP)
    except:
        print("[-] Error : Couldn't resolve : "+tgthost+" : Host unknown")
        return
    setdefaulttimeout(1)
    for port in tgtports:
        t = Thread(target=connScan,args=(tgthost,int(port)))
        t.start()


def main():
    parser = optparse.OptionParser(usage = "Usage : ./portscan.py -H <target> -p <port>")
    parser.add_option("-H",dest='tgthost',help="Specify Target host",type=str)
    parser.add_option("-p",dest='tgtports',help="Specify Target port",type=str)
    options,args = parser.parse_args()

    if( options.tgthost == None or options.tgtports == None ):
        print(parser.usage)
        exit(0)
    else:
        tgthost  = options.tgthost
        tgtports = options.tgtports.split(',')

    portScan(tgthost,tgtports)


if __name__ == "__main__":
    main()
