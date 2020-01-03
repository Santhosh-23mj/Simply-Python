#!/usr/bin/python3

"""
A Recycle Bin Dumper
Module 2 - Correlating SID to Users
"""

from _winreg import *

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
