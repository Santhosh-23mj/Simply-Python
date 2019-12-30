#!/usr/bin/python3

"""
A simple Port Scanner that uses TCP Connect Scan
"""

# Module 1 - Argument Parsing
import optparse
import sys

parser = optparse.OptionParser("Usage :"+sys.argv[0]+" -H <target> -p <port>")
parser.add_option("-H",dest='tgthost',help="Specify Target host",type=str)
parser.add_option("-p",dest='tgtport',help="Specify Target port",type=int)
options,args = parser.parse_args()

tgthost = options.tgthost
tgtport = options.tgtport

if( tgthost == None or tgtport == None ):
    print(parser.usage)
