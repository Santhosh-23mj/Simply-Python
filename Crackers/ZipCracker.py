#!/usr/bin/python3

"""
Program 1
ZipFile Cracker is a simple program to crack password protected ZIP files
"""

import zipfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("zipfile",help = "ZipFile")
parser.add_argument("dictionary",help = "Dictionary\wordlist")
args = parser.parse_args()

zifile   = args.zipfile
dictfile = args.dictionary
    
file2crack = zipfile.ZipFile(zifile)
    
with open( dictfile,'r' ) as passfile:
    for passwd in passfile.readlines():
        passwd = passwd.strip('\n')
        passwd = bytes(passwd,'utf-8')
        try:
            file2crack.extractall(pwd=passwd)
            print("[+] Password Found ==> "+passwd.decode())
            exit(0)
        except:
            pass
