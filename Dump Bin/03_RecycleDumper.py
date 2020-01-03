#!/usr/bin/python3

"""
A Recycle Bin Dumper

This program just prints all the files in Recycle Bin
which could be used for Dumpster Diving
"""

import os
from _winreg import *

# This Function takes in nothing and the returns the
# Directory where the recycle bin is located
def returnDir():
    dirs = ['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    # index 0 = Windows NT, 2000, XP
    # index 1 = Windows 98 and prior FAT System
    # index 2 = Windows Vista,7 and above
    for recycleDir in dirs:
        if( os.path.isdir(recycleDir) ):
            return recycleDir
    return None


# This function takes in the SID and returns
# the user that corresponds to the supplied SID using a reg query
def sid2user(sid):
    try:
        key = OpenKey("HKEY_LOCAL_MACHINE","Software\Microsoft\Windows NT\CurrentVersion\ProfileList\\"+sid)
        value,qtype = QueryValueEx( key, 'ProfileImagePath' )
        user = value.split('\\')[-1]
        return user
    except:
        return sid


# This Function takes in the Recycle Directory and lists the files
# According to the users who deleted those files
def dumpBin(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        user  = sid2user(sid)
        files = os.listdir(recycleDir+sid)
        print("[*] Dumping files for user : " + user)
        for file in files:
            print("[+] Found file : " + str(file))


def main():
    recycleDir = returnDir()
    dumpBin(recycleDir)


if( __name__ == "__main__" ):
    main()
