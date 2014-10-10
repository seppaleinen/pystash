#!/usr/bin/python

import unittest
import sys
from pystash.common import output
from StringIO import StringIO

class testOutputFunction(unittest.TestCase):
	def setUp(self):
		self.held, sys.stdout = sys.stdout, StringIO()

	def testOutputTextOnly_returnString(self):
		result = output("String", text_only=True)
		self.failUnless(result != None)

	def testOutputStdout(self):
		output("String")
		if not hasattr(sys.stdout, "getvalue"):
			self.fail("Need to run in buffered mode")
		result = sys.stdout.getvalue().strip()
		self.assertEquals(result,'String')
        
if __name__ == '__main__':
	unittest.main(module=__name__, buffer=True, exit=False)