#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FileEventHandler():
	def __init__(self):
		pass

	def on_add(self, item):
		#  procedure when an item is added
		print "%s was added." %(item.filename)

	def on_modify(self, item):
		# procedure when an item is modified
		print "%s was modified." %(item.filename)

	def on_move(self, item):
		# procedure when an item is moved
		print "An item was moved to %s" %(item.filename)

	def on_delete(self, item):
		# procedure when an item is deleted
		print "%s was deleted." %(item.filename)