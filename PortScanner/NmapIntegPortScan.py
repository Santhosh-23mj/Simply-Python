#!/usr/bin/python3
"""
A Simple Port Scanner that uses Nmap available in Python
"""

import nmap
import optparse

def nmapScan(host,port):
    nmscan = nmap.PortScanner()
    nmscan.scan(host,port)
    scanres = nmscan[host]['tcp'][port]['state']
    print("[*] "+host+" tcp/"+port+" "+scanres)


def main():
    parser = optparse.OptionParser(usage = "Usage : ./NmapScan.py -H <targethost> -p <targetport>")
    parser.add_option("-H", dest = 'tgthost', type = str, help = "Specify target host to scan")
    parser.add_option("-p", dest = 'tgtport', type = str, help = "Specify list of ports to scan")
    options,args = parser.parse_args()
    
    tgthost = options.tgthost
    tgtport = options.tgtport.split(',')
    
    if( tgthost == None or tgtport == None ):
        print(parser.usage())
        exit(0)
    
    for port in tgtport:
        nmapScan(tgthost,port)  
