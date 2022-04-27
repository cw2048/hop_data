#!/usr/bin/env python


#############
# Run Altering_Hop_Data.ipynb first
# Then remove the first row and column from the csv file. 
#
# Usage: python csv_to_txt.py Monitor02.csv
#
# You will still need to clean up the file after this
##############

#This is the name of the outfile. 
OUT = open("Monitor02.txt", 'w')

import sys
import re

#This prints everything from csv to a txt file. 
for file in sys.argv[1:]:
	IN = open(file, 'r')
	for line in IN:
		line = line.strip("\n")
		line = line.split(",")
		for item in line:
			#To remove the floats from the file
			if re.search(".",item):
				item = item.split(".")
				OUT.write(item[0])
				OUT.write("\t")
			else:
				OUT.write(item)
		OUT.write("\n")
	IN.close()
OUT.close()
