#!/usr/bin/python3

"""
Geolocating using the MAC of APs that we connected
It requires wigle.net account which is a opensource database for 
MAC to Location Lookup
Module 4 - Fetching LAT,LON from wigle.net
"""

import mechanize
import re
import urllib.parse

def fetchLatLon( username, passwd, netid ):
    browser = mechanize.Browser()
    browser.open("http://www.wigle.net")
    reqData = urllib.parse.urlencode({'credential_0':username,'credential_1':passwd})
    browser.open("http://wigle.net/gps/gps/main/login",reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.parse.urlencode(params)
    respUrl   = "http://wigle.net/gps/gps/main/confirmquery"
    resp      = browser.open(respUrl,reqParams).read()
    mapLat    = "N/A"
    mapLon    = "N/A"
    rLat      = re.findall(r'maplat=.*\&',resp)
    if( rLat ):
        mapLat = rLat[0].split("&")[0].split("=")[1]
    rLon      = re.findall(r'maplot=.*\&',resp)
    if( rLon ):
        mapLon = rLon[0].split("&")[0].split("=")[1]
    print("[+] Latitude : " + mapLat + " Longitude : " + mapLon)
    
