#!/usr/bin/env python

OUT = open("Monitor02.txt", 'w')

import sys
import re

for file in sys.argv[1:]:
	IN = open(file, 'r')
	for line in IN:
		line = line.strip("\n")
		line = line.split(",")
		for item in line:
			if re.search(".",item):
				item = item.split(".")
				OUT.write(item[0])
				OUT.write("\t")
			else:
				OUT.write(item)
		OUT.write("\n")
	IN.close()
OUT.close()
