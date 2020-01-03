#!/usr/bin/python3

"""
FireFox DB Data Extractor
Module 3 - Extract Browsing History
"""

import sqlite3

def printHistory(cursor):
    hisQry = "SELECT url,datetime(visit_time/1000000,'unixepoch') FROM moz_places,\
    moz_historyvisits WHERE visit_count > 0 \
    moz_places.id == moz_historyvisits.place_id;"
    cursor.execute(hisQry)
    for row in cursor:
        print("[*] ---------------Found History------------")
        print("     [+] Date    : " + str(row[0]))
        print("     [+] Visited : " + str(row[1]))
    
