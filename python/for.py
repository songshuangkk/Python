#!/usr/bin/python

import sys
import re
import os

suits = {'Bashful':'red','Sneezy':'green','Doc':'blue', 'Dopey':'orage',\
		 'Grumpy':'yellow', 'Happy':'taupe','Sleepy':'puce'}

pattern = re.compile("(%s)"%sys.argv[1])

for dwarf, color in suits.items():
	if pattern.search(dwarf) or pattern.search(color):
		print "%s's dwarf suit is %s."%\
			(pattern.sub(r"_\1_", dwarf),pattern.sub(r"_\1_", color))
		break
else:
	print "No dwarves or dwarf suits matched the pattern"
