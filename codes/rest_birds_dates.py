#!/usr/bin/env python

####
#Run dates.py on bird 1. Then run this on the rest of the birds 
# and finally add them all together with the jupyter notebook. 
#
#Usage: python rest_birds_dates.py b2.txt 2_July*
# The second input if the name of the outfile. 
###

import pandas as pd
import numpy as np
import sys
import re

OUT = open(sys.argv[1], 'w') #Second entry needs to be name of OUT file
OUT.write("b\n")


for file in sys.argv[2:]:
	IN = open(file, 'r')
	#Match dates in file names and group them to add dates into each line
#        match = re.search("(\d+)_(\w+) (\d+), (\d+)", file)
#        year = [match.group(4)]
#        month = [match.group(2)]
#        day = [match.group(3)]
        #CTR = 61355
#        hour = 0
        #Now split by line and add them into one file need 38 numbers separated by tabs for each minute.        #But each number needs to be a new line of 38 numbers
	for line in IN:
		if re.search("^\d+ ",line):
			line = line.strip("\n")
			line = line.split("\t")
	#                hour = hour + 1
	#                minute = 0
			for item in line:
	#                        CTR = CTR + 1
	#                        minute = minute + 1
				OUT.write("%s\n" % (item))
	#			for d in day:
	#                                if len(d) == 1:
	#                                        OUT.write(d[0])
	#                                else:
	#                                        OUT.write(d[0])
	#                                        OUT.write(d[1])
	#                        OUT.write(" ")
	#                        for m in month:
	#                                OUT.write(m[0])
	#                                OUT.write(m[1])
	#                                OUT.write(m[2])
	#                        OUT.write(" ")
	#                        for y in year:
	#                                OUT.write(y[2])
	#                                OUT.write(y[3])
	#                        OUT.write("\t")
	#                        #OUT.write(" %s %s\t" % (month, day))
	#                        #for h in hour:
	#                                #OUT.write(h[0])
	#                                #OUT.write(h[1])
	#                        OUT.write("%s:%s:00\t" % (str(hour).zfill(2), str(minute).zfill(2)))
	#                        OUT.write("1\t")
	#                        OUT.write("%s" % (item))
	#                        OUT.write("\n")
	IN.close()
	#print(day)
	#IN.close()
OUT.close()
