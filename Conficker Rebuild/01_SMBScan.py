#!/usr/bin/python3

"""
Replicating Conficker Worm
Module 1 - Finding Exploitable Targets using Scan
"""

import nmap

def findTargets(subnet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subnet,'445')
    tgthosts = []
    
    for host in nmScan.all_hosts():
        if( nmScan[host].has_tcp(445) ):
            state = nmScan[host]['tcp'][445]['state']
            if( state == 'open' ):
                print("[+] Valid target found : " + host)
                tgthosts.append(host)
    
    return tgthosts
