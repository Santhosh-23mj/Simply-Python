#!/usr/bin/python3

"""
A Simple Windows AP Connections list Enumerator from registry
Module 2 - Printing the Keys
"""

from _winreg import *

def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE,net)
    
    print("[*] Your Networks...")
    for i in range(1,50):
        try:
            guid     = EnumKey(key,i)
            netKey   = OpenKey(key,str(guid))
            n,addr,t = EnumValue(netKey,5)
            n,name,t = EnumValue(netKey,4)
            macAddr  = val2Addr(addr)
            netName  = str(name)
            print("[+]",netName,macAddr,sep=" ")
            CloseKey(netKey)
        except:
            break
