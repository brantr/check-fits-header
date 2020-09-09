#!/usr/bin/env python3
from astropy.io import fits
import sys

fname = "tmp.fits"
if(len(sys.argv)>1):
	fname = sys.argv[1]

print("Checking header for ", fname)

hdulist = fits.open(fname)
header = hdulist[0].header
print(header)
