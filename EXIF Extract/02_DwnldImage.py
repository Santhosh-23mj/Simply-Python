#!/usr/bin/python3

"""
A EXIF data extracter from images in a website
Module 2 - Download all images and store to a file
"""

import urllib
from os.path import basename

def downloadImage(imgTags):
    try:
        print("[+] Downloading Image......")
        imgSrc      = imgTags['src']
        imgReq      = urllib.request.Request(imgSrc)
        imgContent  = urllib.request.urlopen(imgReq)
        imgFilename = basename(urllib.parse.urlsplit(imgSrc)[2])
        with open(imgFilename,'wb') as imgFile:
            imgFile.write(imgContent)
        return imgFilename
    except:
        return
