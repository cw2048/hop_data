#!/usr/bin/env python


import sys
import re

OUT=open("Monitor01.txt", 'w')
CTR = 61355

for file in sys.argv[1:]:
	IN = open(file, 'r')
	match = re.search("(\w+) (\d+), (\d+)", file)
	date = [match.group(2), match.group(1), match.group(3)]
	#CTR = 61355
	time = 0
	for Line in IN:
		#if re.search("^\d+ ", Line):
		Line = Line.strip("\n")
		CTR =+ 1
		time =+ 1
		OUT.write("%d\t" % (CTR))
		OUT.write("%s\t" % (match.group(1)))
		OUT.write("%d\t" % (time))
		OUT.write("1\t")
		OUT.write(Line + "\n")
	IN.close()
OUT.close()

