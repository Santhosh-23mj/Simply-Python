#!/usr/bin/python3

"""
A Simple Windows AP Connections list Enumerator from registry

This Program Simply prints the ESSID and the MAC addresses
of the APs that we connected to, reading all from the registry
"""

from _winreg import *

def val2Addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x" %ord(ch))
    addr = addr.strip(" ").replace(" ",":")[0:17]
    return addr
    
    """
    use this if the above doesnt work
    ls = []
    ls.append(val[0])
    val = val[:12]
    for i in range(len(val)):
        if( i%2 == 0 ):
            ls.append(":")
        ls.append(val[i])
    return ''.join(ls)
    """


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


def main():
    printNets()


if(__name__ == "__main__"):
    main()
