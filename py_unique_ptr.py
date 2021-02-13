#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import sys

class UniquePtr:
	def __init__(self, uniq_object = None):
		self.__obj = uniq_object
		return

	def obj(self):
		if (self.__obj != None):
			assert(sys.getrefcount(self.__obj) == 2)
		return self.__obj

	def move(self):
		o = self.__obj
		self.__obj = None
		return UniquePtr(o)

if __name__ == '__main__':
	assert False, "It is not an executable module"