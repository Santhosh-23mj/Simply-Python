#!/usr/bin/python3

"""
Skype DB Data Extractor

This program opens the Skype Database Directory and opens the 
'main.db' sqlite database and prints our Profile, our Contacts,
our calllogs and our messages
"""

import os
import sqlite3
import argparse

# This Functions takes in the Database as input and
# prints our Profile data
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


# This Function takes in the Database as input and prints
# info about our contacts. Leaving back the NULL 
# values in the database
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


# This Function takes in the Database and prints
# the Call logs. It joins data from two tables
def printLogs(skypeDb):
    logQuery = "SELECT datetime(begin_timestamp,`unixepoch`),identity FROM calls,conversations WHERE calls.conv_dbid = converstions.id;"
    conn     = sqlite3.connect(skypeDb)
    cur      = conn.cursor()
    cur.execute(logQuery)
    print("[*] ------------Found Calls-------------------")
    for row in cur:
        print("[+] Time : " + str(row[0]) + " | Partner : " + str(row[1]))


# This Function takes in database as input and prints out
# our messages with other users
def printMessages(skypeDb):
    mesQuery = "SELECT datetime(timestamp,'unixepoch'),dialog_partner,author,body_xml FROM Message;"
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Path",type = str, help = "Specify Path to SkypeDirectory")
    args = parser.parse_args()
    
    path = args.Path
    
    if( os.path.isdir(path) == False ):
        print("[!] Not a valid path : " + path)
        exit(0)
    else:
        skypeDb = os.path.join(path,'main.db')
        if( os.path.isfile(skypeDb) ):
            printProfile(skypeDb)
            printContacts(skypeDb)
            printLogs(skypeDb)
            printMessages(skypeDb)
        else:
            print("[!] Skype DB doesn't exist " + skypeDb)
            exit(0)


if( __name__ == "__main__" ):
    main()
