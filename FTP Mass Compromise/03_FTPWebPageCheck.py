#!/usr/bin/python3

"""
FTP Mass Compromise replication of k985ytv infection
Module 3 - FTP Web Page Checker
"""

import ftplib

def retDefault(ftp):
    try:
        lisDir = ftp.nlst()
    except:
        print("[-] Couldn't list directory contents")
        return
    retDir = []
    for files in lisDir:
        names = files.lower()
        if( '.php' in names or '.htm' in names or '.asp' in names ):
            retDir.append(files)
            print("[+] Found a WebPage : "+files)
    return retDir


def main():
    host   = ''
    user   = ''
    passwd = ''
    
    ftp = ftplib.FTP(host)
    ftp.login(user,passwd)
    retDefault(ftp)
