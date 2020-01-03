#!/usr/bin/python3

"""
Skype DB Data Extractor
Module 1 - Print our Profile Data
"""

import sqlite3

def printProfile(skypeDb):
    profileQuery = "SELECT fullname,skypename,city,country,datetime(profile_timestamp,`unixepoch`) FROM Accounts;"
    conn         = sqlite3.connect(skypeDb)
    cur          = conn.cursor()
    cur.execute(profileQuery)
    for row in cur:
        print("[*] ---------------Account Found---------------")
        print("[+] User           : " + str(row[0]))
        print("[+] Skype Username : " + str(row[1]))
        print("[+] Location       : " + str(row[2]) + ", " + str(row[3]))
        print("[+] Profile Date   : " + str(row[4]))
