#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import re


OUT=open("Monitor01.txt", 'a')

for old_lin in OUT:
	for file in sys.argv[1:]:
		IN = open(file, 'r')
		for line in IN:
			line = line.strip("\n")
			OUT.write("%s\n" % (line))
	IN.close()
OUT.close()
