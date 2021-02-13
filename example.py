#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from py_unique_ptr import *

class Foo:
	def get_string(self):
		return "123"

def main(args):
	p1 = UniquePtr(Foo())
	p2 = UniquePtr()
	print(f"p1={p1.obj()}")
	print(f"p2={p1.obj()}")
	print(f"get_string={p1.obj().get_string()}")
	print("")
	p2 = p1.move()
	print(f"p1={p1.obj()}")
	print(f"p2={p1.obj()}")
	print(f"get_string={p2.obj().get_string()}")
	print("")
	p3 = p2.obj()
	# дальше сработает ассерт
	print(f"get_string={p2.obj().get_string()}")
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))