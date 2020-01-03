#!/usr/bin/python3

"""
FireFox DB Data Extractor
Module 4 - Print Searches
"""

import re

def printSearches(cursor):
    hisQry = "SELECT url,datetime(visit_time/1000000,'unixepoch') FROM moz_places,\
    moz_historyvisits WHERE visit_count > 0 \
    moz_places.id == moz_historyvisits.place_id;"
    cursor.execute(hisQry)
    print("[*] ------------------Google Searches Found--------------")
    for row in cursor:
        url  = str(row[0])
        time = str(row[1])
        if( 'google' in url.lower() ):
            reg = re.findall(r'q=.*\&',url)
            if( reg ):
                search = reg[0].split('&')[0]
                search = search.replace("q=","").replace("+"," ")
                print("    [+] Time         : "+ time)
                print("    [+] Searched For : "+ search)
