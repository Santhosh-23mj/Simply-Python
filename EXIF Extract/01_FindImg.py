#!/usr/bin/python3

"""
A EXIF data extracter from images in a website
Module 1 - Get all inage tags in a website
"""

import urllib2
from bs4 import BeautifulSoup

def findImages(url):
    print("[+] Finding Images on " + url)
    urlContent = urllib2.urlopen(url).read()
    # req  = urllib.request.Request(url)
    # resp = urllib.request.urlopen(req)
    soup       = BeautifulSoup(urlContent)
    imgTags    = soup.find_all('img')
    return imgTags
