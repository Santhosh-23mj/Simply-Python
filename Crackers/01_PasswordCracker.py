#!/usr/bin/python3

"""
Program 1
The UNIX Password cracker where the passwords are just hashed using the
crypt() in UNIX using a 2 character hash.
"""

import os
import sys
import crypt

def crackpass(cryptpass,dictfile):
    salt = str(cryptpass[0:2])
    print("    [*] Salt : "+salt)
    print("    [*] Hash : "+str(cryptpass[2:]))
    with open(dictfile) as passfile:
        for passwd in passfile.readlines():
            passwd   = passwd.strip()
            passwd   = passwd.strip('\n')
            calchash = crypt.crypt(passwd,salt)
            if( calchash == cryptpass ):
                print("[+] Password found ==> "+passwd)
                print("===========================================")
                return
        print("[-] Exhausted Wordlist try a better one!!")
    


def main():
    if(len(sys.argv) == 3):
        file2crack = str(sys.argv[1])
        dictfile   = str(sys.argv[2])
        if not os.access(file2crack,os.F_OK):
            print("[-] Can't access file "+file2crack)
            exit(0)
        if not os.access(dictfile,os.F_OK):
            print("[-] Can't access file "+dictfile)
            exit(0)
    else:
        print("Usage : "+str(sys.argv[0]+" <hashfile> <dictionary>"))
        print("Please Dont Change the Order")
    
    with open(file2crack,'r') as hashfile:
        for line in hashfile.readlines():
            if( ":"  in line ):
                user      = line.split(":")[0]
                cryptpass = line.split(":")[1]
                print("[+] Cracking password for "+user)
                crackpass(cryptpass,dictfile)
                

if __name__ == '__main__':
    main()
