#!/usr/bin/python

import sys
import string

class Ary(object):
	"""docstring for Ary"""

	def select(self, arg = None):
		if arg == None:
			print "There is no data"
		elif arg[0] == '0' and (arg[1] == 'x' or arg[1] == 'X'):
			arg = arg[2:]
			self.Ary16(arg)
		else:
			self.Ary10(arg)

	def Ary16(self, arg):
		l = len(arg)
		t = 0
		for s in arg:
			if self.table_10.has_key(s):
				s = self.table_10[s]
			t = string.atoi(s)*(16**(l-1)) + t
			l = l - 1
		self.s = str(t)
		print self.s
			
		
	def Ary10(self, arg):
		num = string.atoi(arg)
		while num != 0:
			t = num % 16
			if t >= 10 and t <= 15:
				t = str(t)
				self.s = self.s + self.table_16[t]
			else:
				t = str(t)
				self.s = self.s + t
			num = num / 16

		self.s = self.s + "x0"
		self.s = self.s[::-1]

		print self.s

	def __init__(self, arg = None):
		self.s = ""
		self.table_16 = {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}
		self.table_10 = {"A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"}
		None


if __name__ == '__main__':
	try:
		ary = Ary(sys.argv[1])
	except Exception, SyntaxError:
		print "There is no data"
	else:
		ary.select(sys.argv[1])
