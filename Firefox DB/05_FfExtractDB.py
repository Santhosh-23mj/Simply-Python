#!/usr/bin/python3

"""
FireFox DB Data Extractor

This program opens the Firefox's storage directory
Opens the Sqlite databases and prints the 
browser history, google searches, cookies and the downloads
as available in the Databases
"""

import os
import re
import sqlite3
import argparse

# This function gets in the DB name and makes a connection 
# and returns the object prints error if cant open DB
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


# This function gets the cursor and prints all the downloads
def printDownloads(cursor):
    dwnldQry = "SELECT name,source,datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
    cursor.execute(dwnldQry)
    for row in cursor:
        print("[*] ------------Downloaded Files-------------")
        print("    [+] File : " + str(row[0]))
        print("    [+] From : " + str(row[1])) 
        print("    [+] at   : " + str(row[2]))


# This function takes in the cursor as input and prints all the cookies
def printCookies(cursor):
    cookQry = "SELECT host,name,value FROM moz_cookies"
    cursor.execute(cookQry)
    for row in cursor:
        print("[*] -------------Found Cookies----------------")
        print("    [+] Host  : "+ str(row[0]))
        print("    [+] Name  : "+ str(row[1]))
        print("    [+] Value : "+ str(row[2]))


# This function takes in the cursor and prints all the Google Search Queries
# from the Search history
def printSearches(cursor):
    hisQry = "SELECT url,datetime(visit_time/1000000,'unixepoch') FROM moz_places,\
    moz_historyvisits WHERE visit_count > 0 \
    moz_places.id == moz_historyvisits.place_id;"
    cursor.execute(hisQry)
    print("[*] ------------------Google Searches Found--------------")
    for row in cursor:
        url  = str(row[0])
        time = str(row[1])
        # print(time,url,sep=":") if u want browsing history :)
        if( 'google' in url.lower() ):
            reg = re.findall(r'q=.*\&',url)
            if( reg ):
                search = reg[0].split('&')[0]
                search = search.replace("q=","").replace("+"," ")
                print("    [+] Time         : "+ time)
                print("    [+] Searched For : "+ search)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Dir", type = str, help = "Path to the Mozilla Firefox Profile")
    args = parser.parse_args()
    
    path = args.Dir
    
    dwnlds  = "downloads.sqlite"
    cookies = "cookies.sqlite"
    history = "places.sqlite"
    
    if( os.path.isdir(path) == False ):
        print("[!] Path or Directory doesn't exist")
        exit(0)
    else:
        dwnldsSql = os.path.join(path,dwnlds)
        if( os.path.isfile(dwnldsSql) ):
            printDownloads(dbConnect(dwnldsSql))
        else:
            print("[!] Downloads DB doesn't exist")
        
        cookiesSql = os.path.join(path,cookies)
        if( os.path.isfile(cookiesSql) ):
            printCookies(dbConnect(cookiesSql))
        else:
            print("[!] Cookies DB doesn't exist")
        
        historySql = os.path.join(path,history)
        if( os.path.isfile(historySql) ):
            printSearches(dbConnect(historySql))
        else:
            print("[!] Places DB doesn't exist")


if( __name__ == "__main__" ):
    main()
