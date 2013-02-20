#!/usr/bin/python

import os, sys, binascii

def ispcap():
    global magic
    begin = f.read(4)
    magic = binascii.hexlify(begin)
    if (magic == "0a0d0d0a"):
	f.seek(8)
	magic = binascii.hexlify(f.read(4))[::-1]
	print file, "is PCAP-NG(NTAR)\nMagic #:",magic
    elif (magic == "a1b2c3d4") or (magic == "d4c3b2a1"):
	print file, "is PCAP file\nMagic #:",magic
    elif (magic == "12cbe2a1"):
	print file, "is Netsniff-NG PCAP file\nMagic #:",magic
    else:
        sys.exit(0)

file = sys.argv[1]
print "\n+MetaCapNG+\n|A Simple PCAP Meta Data Extractor|"
print "\nUsage:", os.path.basename(__file__), "<pcap>\n"

f = open(file, "rb")
ispcap()

# PCAP-NG
if (magic == "a1b2c3d4"):
    f.seek(4,0)
    print binascii.hexlify(f.read(4))
    print f.read(4)
    f.seek(12,0)
    vers = binascii.hexlify(f.read(4))
    print "Major/Minor Version: |",vers
    f.seek(28,0)
    app = f.read(14)
    print "Application(shb_userappl): |",app
    f.seek(72,0)
    int = f.read(10)
    print "Interface(if_name): |",int

# Netsniff-NG
if (magic == "12cbe2a1"):
    data = f.read(100)
    print data

f.close()	
