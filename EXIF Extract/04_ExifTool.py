#!/usr/bin/python3

"""
A EXIF data extracter from images in a website

This program takes an url and scrapes it for image tags
Downloads all the images and extracts the GPS info
from those images. we could also print all the data
associated with the image by making a small change
"""

import sys
import urllib
import optparse
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

# This Function takes in the URL as input 
# and returns all the image tags in the site
def findImages(url):
    print("[+] Finding Images on " + url)
    urlContent = urllib2.urlopen(url).read()
    # req  = urllib.request.Request(url)
    # resp = urllib.request.urlopen(req)
    soup       = BeautifulSoup(urlContent)
    imgTags    = soup.find_all('img')
    return imgTags


# This function gets the URL of images and 
# downloads all the images and opens a file and writes images
# to it in Binary Mode
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


# This Function takes in the image as input and 
# extracts GPS data out of it if available
def getExif(imgFilename):
    try:
        exif    = {}
        imgFile = Image.open(imgFilename)
        exInfo  = imgFile._getexif()
        if( exInfo ):
            for tag,value in exInfo.items():
                decoded = TAGS.get( tag, tag )
                exif[decoded] = value
                # print exif if u want all the EXIF data
            exifGps = exif['GPSInfo']
            if( exifGps ):
                print("[+] GPS Info for " + imgFilename +" : " + exifGps)
    except:
        pass


def main():
    parser = optparse.OptionParser(usage = "Usage : %s -u <url> " %sys.argv[0])
    parser.add_option("-u",dest = 'url', type = str, help = "Specify URL to extract GPS data")
    options,args = parser.parse_args()
    
    if( options.url == None ):
        print(parser.usage)
        exit(0)
    else:
        imgTags = findImages(options.url)
        for imgTag in imgTags:
            imgFile = downloadImage(imgTag)
            getExif(imgFile)


if( __name__ == '__main__' ):
    main()
