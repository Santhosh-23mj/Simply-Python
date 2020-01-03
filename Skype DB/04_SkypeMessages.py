#!/usr/bin/python3

"""
Skype DB Data Extractor
Module 4 - Print our Messages
"""

import sqlite3

def printMessages(skypeDb):
    mesQuery = "SELECT datetime(timestamp,`unixepoch`),dialog_partner,author,body_xml FROM Message;"
    conn     = sqlite3.connect(skypeDb)
    cur      = conn.cursor()
    cur.execute(mesQuery)
    print("[*] --------------Found Messages---------------")
    for row in cur:
        try:
            if("partlist" not in str(row[3])):
                if( str(row[1]) != str(row[2]) ):
                    msgDir = "To : " + str(row[2]) + " : "
                else:
                    msgDir = "From : " + str(row[2]) + " : "
                print("[+] Time : " + str(row[0]) + " " + msgDir + str(row[3]))
        except:
            pass
