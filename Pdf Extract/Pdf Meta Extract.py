#!/usr/bin/python3

""""
PDF metadata extracter

This program just prints the Metadata in a PDF file
The pyPdf library isn't working properly
"""

import optparse
from pyPdf import PdfFileReader

# This function takes in the filename
# and prints out the Metadata of the file
def printMeta(filename):
    pdfFile = PdfFileReader(file(filename,'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print("[*] The Metadata for " + str(filename))
    for metaItem in docInfo:
        print("[+] "+ metaItem[0] + ":" + docInfo[metaItem])


def main():
    parser = optparse.OptionParser(usage="Usage %prog -f <filename>")
    parser.add_option('-f', dest = 'filename', type = str, help = "Specify the file to extract metadata")
    options,args = parser.parse_args()
    
    filename = options.filename
    if( filename == None ):
        print(parser.usage)
        exit(0)
    else:
        printMeta(filename)


if( __name__ == '__main__' ):
    main()
