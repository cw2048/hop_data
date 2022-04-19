#!/usr/bin/env python


#####
# First run python by_bird.py to separate all the birds into individual files.
#
# Then run this script to add all individual birds by dates together.
#
# Usage: python dates.py (ALL of what ever bird)
#
##############


import pandas as pd
import numpy as np
import sys
import re

OUT = open("Monitor01.txt", 'w')
CTR = 61354


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
		line = line.strip("\n")
		line = line.split("\t")
		hour = hour + 1
		minute = 0
		for item in line:
			CTR = CTR + 1
			minute = minute + 1
			OUT.write("%d\t" % (CTR))
			OUT.write("%s %s %s\t" % (year, month, day))
			OUT.write("%s:%s:00\t" % (hour, minute))
			OUT.write("1\t")
			OUT.write("%s" % (item))
			OUT.write("\n")
	IN.close()
	print(day)
	#IN.close()
OUT.close()
