#!/usr/bin/python

import sys
import os

def show_usage(message, code = 1):
	print message
	print "%s: source_dir dest_dir"%sys.argv[0]
	sys.exit(code)

if len(sys.argv) != 3:
	show_usage("2 arguments required you supplied %d"%((len(sys.argv))-1))
elif not os.path.isdir(sys.argv[1]):
	show_usage("Invalid source directory")
elif not os.path.isdir(sys.argv[2]):
	show_usage("Invalid destination directory")

source, dest = sys.argv[1:3]

print "Source Directory is", source
print "Destination Directory is", dest
