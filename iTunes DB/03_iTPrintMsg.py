#!/usr/bin/python3

"""
iTunes Backup Message Extractor
Module 3 - Print Messages from found Message table
"""

def printMessages(cursor):
    msgQry = "SELECT datetime(date,'unixepoch'),address,text FROM message WHERE address > 0;"
    cursor.execute(msgQry)
    for row in cursor:
        print("[+] Date    : " + str(row[0]))
        print("[+] Address : " + str(row[1]))
        print("[+] Text    : " + str(row[2]))
    
