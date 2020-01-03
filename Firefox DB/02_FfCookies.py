#!/usr/bin/python3

"""
FireFox DB Data Extractor
Module 2 - Extract Cookies
"""

import sqlite3

def dbConnect(dataBase):
    try:
        conn  = sqlite3.connect(dataBase)
        cur   = conn.cursor()
        return cur
    except Exception as e:
        if( "encrypted" in str(e) ):
            print("[-] Error Reading database.")
            print("[!] Update your Python-Sqlite3 library > 3.6")
            exit(0)


def printCookies(cursor):
    cookQry = "SELECT host,name,value FROM moz_cookies"
    cursor.execute(cookQry)
    for row in cursor:
        print("[*] -------------Found Cookies----------------")
        print("    [+] Host  : "+ str(row[0]))
        print("    [+] Name  : "+ str(row[1]))
        print("    [+] Value : "+ str(row[2]))
