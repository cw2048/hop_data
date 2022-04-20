#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import re

for file in sys.argv[1:]:
	IN = open(file, 'r')
	match = re.search("(\d+)_(\w+) (\d+), (\d+)", file)
	date = [match.group(2), match.group(1), match.group(3)]
	CTR = 0
	time = 0
	#OUT=open("out.txt", 'w')
	for Line in IN:
		if re.search("^\d+ ", Line):
		#Line = Line.strip("\n")
		#CTR =+ 1
		#time =+ 1
		#OUT.write("%d\t" % (CTR))
		#OUT.write("%s\t" % (match.group(1)))
		#OUT.write("%d\t" % (time))
		#OUT.write("1\t")
		#OUT.write(Line + "\n")
	print(date)
	#IN.close()
#OUT.close()
