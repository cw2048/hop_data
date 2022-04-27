#!/usr/bin/env python


#####
# First run python bybird.py to separate all the birds into individual files.
#
# Then run this script to add all individual birds by dates together.
#
# Usage: python dates.py 1_July*
# python dates.py 2_July*
# etc. ...
#
# (ALL of whatever bird)
#
##############


import pandas as pd
import numpy as np
import sys
import re

#Output will be all in one text file
OUT = open("Monitor01.txt", 'w')
#counter may not need to start here, but it matches another file
CTR = 61354
#Need a header for csv conversion and back
OUT.write("header\n")

#Pull in each bird file (by_bird.py adds the number to the begining of all files, so 2_* is all
#the dates for the second bird.

for file in sys.argv[1:]:
	IN = open(file, 'r')
	#Match dates in file names and group them to add dates into each line
	match = re.search("(\d+)_(\w+) (\d+), (\d+)", file)
	year = [match.group(4)]
	month = [match.group(2)]
	day = [match.group(3)]
	#CTR = 61355
	hour = 0
	#Now split by line and add them into one file need 38 numbers separated by tabs for each minute.
	#But each number needs to be a new line of 38 numbers
	for line in IN:
		if re.search("^\d+ ",line):
			line = line.strip("\n")
			line = line.split("\t")
			minute = 0
#			while minute < 61:
			#There is an extra space at the end of each 1 bird. This removes it
			line.pop()
			for item in line:
#				if item.isdigit():
				CTR = CTR + 1
				OUT.write("%d\t" % (CTR))
				#getting 1 digit days
				#s = 1
				#str_day = [str(da) for da in day]
				#a_str_day = "".join(str_day)
				#int_day = int(a_str_day)
				for d in day:
					if len(d) == 1:
						OUT.write(d[0])
					else:
						OUT.write(d[0])
						OUT.write(d[1])
				OUT.write(" ")
				for m in month:
					OUT.write(m[0])
					OUT.write(m[1])
					OUT.write(m[2])
				OUT.write(" ")
				for y in year:
					OUT.write(y[2])
					OUT.write(y[3])
				OUT.write("\t")
				#OUT.write(" %s %s\t" % (month, day))
				#for h in hour:
					#OUT.write(h[0])
					#OUT.write(h[1])
				OUT.write("%s:%s:00\t" % (str(hour).zfill(2), str(minute).zfill(2)))
				OUT.write("1\t")
				OUT.write("%s" % (item))
				OUT.write("\n")
				minute = minute + 1
#		else:
#			do_nothing = 0
			hour = hour + 1
	IN.close()
	print(day) #Check to see if it worked
	#IN.close()
OUT.close()
