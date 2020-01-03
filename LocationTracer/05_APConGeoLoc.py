#!/usr/bin/python3

"""
Geolocating using the MAC of APs that we connected
It requires wigle.net account which is a opensource database for 
MAC to Location Lookup

This program prints the Latitude and Longitude of the MAC addresses of the
APs that we connected to from public database called wigle which could fetch
the locations of where we have been :)
"""

import re
import sys
import optparse
import mechanize
import urllib.parse
from _winreg import *

# Convert REG BINARY to MAC
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


# Get the Latitude and Longitude from the MAC Address
def fetchLatLon( username, passwd, netid ):
    browser = mechanize.Browser()
    browser.open("http://www.wigle.net")
    reqData = urllib.parse.urlencode({'credential_0':username,'credential_1':passwd})
    browser.open("http://wigle.net/gps/gps/main/login",reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.parse.urlencode(params)
    respUrl   = "http://wigle.net/gps/gps/main/confirmquery"
    resp      = browser.open(respUrl,reqParams).read()
    mapLat    = "N/A"
    mapLon    = "N/A"
    rLat      = re.findall(r'maplat=.*\&',resp)
    if( rLat ):
        mapLat = rLat[0].split("&")[0].split("=")[1]
    rLon      = re.findall(r'maplot=.*\&',resp)
    if( rLon ):
        mapLon = rLon[0].split("&")[0].split("=")[1]
    print("[+] Latitude : " + mapLat + " Longitude : " + mapLon)


# Print out the AP Connections and their MAC From Registry
def printNets( username, passwd ):
    net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
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
            fetchLatLon( username, passwd, macAddr )
            CloseKey(netKey)
        except:
            break


def main():
    parser = optparse.OptionParser(usage = "Usage : python3 %s -u <username> -p <password>" %sys.argv[0])
    parser.add_option("-u", dest = 'username', type = str, help = "Specify username for wigle.net")
    parser.add_option("-p", dest = 'passwd', type = str, help = "Specify password for wigle.net")
    options,args = parser.parse_args()
    
    username = options.username
    passwd   = options.passwd
    
    if( username == None or passwd == None ):
        print(parser.usage)
        exit(0)
    else:
        printNets( username, passwd )


if( __name__ == "__main__" ):
    main()
