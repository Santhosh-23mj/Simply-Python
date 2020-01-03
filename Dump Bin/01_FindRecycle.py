#!/usr/bin/python3

"""
A Recycle Bin Dumper 
Module 1 - Find the Recycle Bin Directory
"""

import os

# This Function takes in nothing and the returns the
# Directory where the recycle bin is located
def returnDir():
    dirs = ['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if( os.path.isdir(recycleDir) ):
            return recycleDir
    return None
