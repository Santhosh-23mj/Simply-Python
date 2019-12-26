#!/usr/bin/python3

"""
Program 2
The UNIX Password cracker No work to be done.
The Program itself determines hash type and uses dictionary to bruteforce the password
"""

import os
import sys
import crypt

print("-----------------------------")
print("|   *NIX Password Cracker   |")
print("|           -_-             |")
print("-----------------------------")
def crackpass(cryptpass,dictfile):
    hashedpass = cryptpass.split("$")
    hashindic  = hashedpass[1]
    hashtype   = {'1':"MD5",'2a':"BlowFish",'5':"SHA-256",'6':"SHA-512"}
    
    salt = "$"+hashindic+"$"+hashedpass[2]
    
    print("    [*] Salt ==> "+salt)
    print("    [*] $"+hashedpass[1]+"$  ==> "+str(hashtype[hashindic]))
    print("    [*] Hash ==> "+hashedpass[3])
    
    with open(dictfile) as passfile:
        for passwd in passfile.readlines():
            #passwd   = passwd.strip()
            passwd   = passwd.strip('\n')
            calchash = crypt.crypt(passwd,salt)
            if( calchash == cryptpass ):
                print("[+] Password found ==> "+passwd)
                print("="*len(hashedpass[3]))
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
        print("Usage : "+str(sys.argv[0])+" <hashfile> <dictionary>")
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
