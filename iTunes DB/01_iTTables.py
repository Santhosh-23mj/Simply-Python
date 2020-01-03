#!/usr/bin/python3

"""
iTunes Backup Message Extractor
Module 1 - Print all tables
"""

import os
import sqlite3

def dbConnect(file):
    try:
        conn = sqlite3.connect(file)
        curs = conn.cursor()
        return curs
    except:
        return None


def printTables(cursor,file):
    tblQry = "SELECT tbl_name FROM sqlite_master WHERE type == \"table\";"
    cursor.execute(tblQry)
    print("[+] DataBase Found : " + file)
    for row in cursor:
        print("    [+] Table found : " + str(row))


dirList = os.listdir(os.getcwd())
for file in dirList:
    cursor = dbConnect(file)
    if( cursor != None ):
        printTables(cursor,file)
