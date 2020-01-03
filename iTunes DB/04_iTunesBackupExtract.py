#!/usr/bin/python3

"""
iTunes Backup Message Extractor

This Program opens the iTunes Backup directory and
searches for sqlite Databases. If a Sqlite database 
is found it searches for messages Table in that DB
if found prints the Messages
"""

import os
import argparse
import sqlite3


# This function connects to the DB and returns Connection cursor
# returns none if it is not a database or any error in connection
def dbConnect(file):
    try:
        conn = sqlite3.connect(file)
        curs = conn.cursor()
        return curs
    except Exception as e:
        if('encrypted' in str(e)):
            print("[-] Error While reading : " + file)
            print("[!] Update python-sqlite3 library")
            return None
        else:
            return None


# This function takes in the cursor and returns true if the 
# database contains a message table else returns false
def hasMessageTable(cursor):
    tblQry = "SELECT tbl_name FROM sqlite_master WHERE type=\"table\";"
    cursor.execute(tblQry)
    for row in cursor:
        if( 'message' in str(row) ):
            return True
    return False


# This function takes in the cursor and prints all the Messages
# from the messages Table
def printMessages(cursor):
    msgQry = "SELECT datetime(date,'unixepoch'),address,text FROM message WHERE address > 0;"
    cursor.execute(msgQry)
    for row in cursor:
        print("    [+] Date    : " + str(row[0]))
        print("    [+] Address : " + str(row[1]))
        print("    [+] Text    : " + str(row[2]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Path", type = str, help = "Specify iTunes Backup Directory")
    args = parser.parse_args()
    
    path = args.Path
    
    if( os.path.isdir(path) == False ):
        print("[-] Invalid Path!")
        exit(0)
    else:
        dirList = os.listdir(path)
        for file in dirList:
            fullPath = os.path.join(path,file)
            cursor   = dbConnect(fullPath)
            if( cursor != None ):
                if( hasMessageTable(cursor) ):
                    print("[*] Found DB with Messages " + file)
                    printMessages(cursor)


if( __name__ == "__main__" ):
    main()
