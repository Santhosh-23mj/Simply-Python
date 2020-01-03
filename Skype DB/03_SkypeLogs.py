#!/usr/bin/python3

"""
Skype DB Data Extractor
Module 3 - Print our Call Logs
"""

import sqlite3

def printLogs(skypeDb):
    logQuery = "SELECT datetime(begin_timestamp,`unixepoch`),identity FROM calls,conversations WHERE calls.conv_dbid = converstions.id;"
    conn     = sqlite3.connect(skypeDb)
    cur      = conn.cursor()
    cur.execute(logQuery)
    print("[*] ------------Found Calls-------------------")
    for row in cur:
        print("[+] Time : " + str(row[0]) + " | Partner : " + str(row[1]))
