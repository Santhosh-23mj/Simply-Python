#!/usr/bin/python3

"""
A Simple Windows AP Connections list Enumerator from registry
Module 1 - REG_BINARY to MAC Conversion
"""

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
