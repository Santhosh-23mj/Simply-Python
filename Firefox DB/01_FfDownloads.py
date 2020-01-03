#!/usr/bin/python3

"""
FireFox DB Data Extractor
Module 1 - Extract Downloads

Firefox uses the Sqlite3 DB to store all things like browser sessions, cookies, 
Downloads, Browsing History etc.., which serves a wealth of information and 
We'll Extract some things that will be valuable for us.
"""

import sqlite3

def dbConnect(dataBase):
    conn  = sqlite3.connect(dataBase)
    cur   = conn.cursor()
    return cur


def printDownloads(cursor):
    dwnldQry = "SELECT name,source,datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
    cursor.execute(dwnldQry)
    for row in cursor:
        print("[*] ------------Downloaded Files-------------")
        print("    [+] File : " + str(row[0]))
        print("    [+] From : " + str(row[1])) 
        print("    [+] at   : " + str(row[2]))
