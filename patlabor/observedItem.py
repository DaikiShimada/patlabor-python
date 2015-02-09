#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

class ObservedItem():
	def __init__ (self, filename):
		self.filename = os.path.abspath(filename)	
		self.time = os.path.getmtime(filename)

	def __eq__(self, item):
		# Overlaoding of equal operation
		return self.filename == item.filename

	def isModified(self, item):
		# cheking the time-stamps
		return self.time < item.time

	def isMoved(self, item):
		# return bool of being moved
		if self.filename.split('/')[-1] == item.filename.split('/')[-1]:
			return os.path.dirname(self.filename) != os.path.dirname(item.filename)
		return False