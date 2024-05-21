#!/usr/bin/env python3
from astropy.io import fits
import sys

fname = "tmp.fits"
if(len(sys.argv)>1):
	fname = sys.argv[1]

print("Checking header for ", fname)

hdulist = fits.open(fname)

hdulist.info()

header = hdulist[0].header
#print(header)
print(repr(header))
#for l in header.keys():
#	print(l,header[l])

if(len(hdulist)>1):
    for i in range(len(hdulist)):
        header = hdulist[i].header
        print(repr(header))
#for l in header.keys():
#    print(l,header[l])
