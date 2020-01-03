#!/usr/bin/python3

"""
Skype DB Data Extractor
Module 2 - Print our Contacts
"""

import sqlite3

def printContacts(skypeDb):
    conQuery = "SELECT displayname,skypename,city,country,phone,mobile,birthday FROM Contacts;"
    conn     = sqlite3.connect(skypeDb)
    cur      = conn.cursor()
    cur.execute(conQuery)
    for row in cur:
        print("[*] --------------Found Contact-------------")
        print("[+] User           : " + str(row[0]))
        print("[+] Skype Username : " + str(row[1]))
        if( row[2] != '' and row[2] != None ):
            print("[+] Location        : " + str(row[2]) + "," + str(row[3]))
        if( row[4] != None ):
            print("[+] Mobile          : " + str(row[4]))
        if( row[5] != None ):
            print("[+] Birthday        : " + str(row[5]))
