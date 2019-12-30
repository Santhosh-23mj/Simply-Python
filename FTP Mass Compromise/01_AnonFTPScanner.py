#!/usr/bin/python3

"""
FTP Mass Compromise replication of k985ytv infection
Module 1 - An Anonymous FTP Scanner
"""

import ftplib
import optparse

def anonLogin(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user="Anonymous",passwd=" ")
        print("[+] Anonymous Login succeeded !")
        print("Host : "+host)
        ftp.quit()
        return
    except:
        print("[+] Anonymous Login failed ")
        return


def main():
    parser = optparse.OptionParser(usage = "Usage : ./FtpScan.py -H <hosts>")
    parser.add_option("-H", dest = 'host', type = str, help = "Speciy a list of hosts seperated by commas")
    options,args = parser.parse_args()
    
    hosts = options.host.split(',')
    
    if( hosts == None ):
        print(parser.usage)
        exit(0)
    
    for target in hosts:
        anonLogin(target)
