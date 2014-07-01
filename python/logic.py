#!/usr/bin/python
#-*-coding:utf-8-*-

"""逻辑计算器"""

import sys
import string

table = {"A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"}

class Logic(object):
	"""docstring for Logic"""
	def __init__(self, *arg):
		None

	def operator(self, *arg):
		while True:
			print "Please input your choice:"
			print "1. Function And"
			print "2. Function Or"
			print "3. Function Xor"
			select = input("Your choice:")
			if select == 1:
				return (arg[0] & arg[1])
			elif select == 2:
				return (arg[0]| arg[1])
			elif select == 3:
				return (arg[0] ^ arg[1])
			else:
				continue

def Process(*arg):
	s1 = arg[0].upper()
	s2 = arg[1].upper()
	if (s1[0] == '0' and s1[1] == 'X') or (s2[0] == '0' and s2[1] == 'X'):
		if s1[:2] == "0X":
			s1 = list(s1)
			n = 2
			for x in s1[2:]:
				if table.has_key(x):
					s1[n] = table[x]
				n = n + 1
			s1 = ''.join(s1)

		if s2[:2] == "0X":
			s2 = list(s2)
			n = 2
			for x in s2[2:]:
				if table.has_key(x):
					s2[n] = table[x]
				n = n + 1
			s2 = ''.join(s2)
			s1 = int(s1, 16)
			s2 = int(s2, 16)
			return s1, s2
	else:
		s1 = list(s1)
		n = 0
		for x in s1:
			if table.has_key(x):
				s1[n] = table[x]
				n = n + 1
		s1 = ''.join(s1)
		s2 = list(s2)
		n = 0
		for x in s2:
			if table.has_key(x):
				s2[n] = table[x]
				n = n + 1
		s2 = ''.join(s2)

		s1 = int(s1, 16)
		s2 = int(s2, 16)
		return s1, s2

	return string.atoi(s1), string.atoi(s2)

if __name__ == '__main__':
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]

	arg1, arg2 = Process(arg1, arg2)
	
	logic = Logic(arg1, arg2)

	print logic.operator(arg1, arg2)
	
	