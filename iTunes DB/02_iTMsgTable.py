#!/usr/bin/python3

"""
iTunes Backup Message Extractor
Module 2 - Search for Messages Table
"""

def hasMessageTable(cursor):
    tblQry = "SELECT tbl_name FROM sqlite_master WHERE type=\"table\";"
    cursor.execute(tblQry)
    for row in cursor:
        if( 'message' in str(row) ):
            return True
