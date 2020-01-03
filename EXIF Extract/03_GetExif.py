#!/usr/bin/python3

"""
A EXIF data extracter from images in a website
Module 3 - Extract EXIF using PIL
"""

from PIL import Image
from PIL.ExifTags import TAGS

def getExif(imgFilename):
    try:
        exif    = {}
        imgFile = Image.open(imgFilename)
        exInfo  = imgFile._getexif()
        if( exInfo ):
            for tag,value in exInfo.items():
                decoded = TAGS.get( tag, tag )
                exif[decoded] = value
            exifGps = exif['GPSInfo']
            if( exifGps ):
                print("[+] GPS Info for " + imgFilename +" : " + exifGps)
    except:
        pass
