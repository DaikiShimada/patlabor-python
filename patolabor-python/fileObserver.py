#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys
import threading

from observedItem import *
from fileEventHandler import * 

def getExt(filename):
	# return extention of file
	return os.path.splitext(filename)[-1].lower()

class FileObserver(threading.Thread):
	def __init__ (self):
		super(FileObserver, self).__init__()
		self.stop_event = threading.Event()

		self.handler = None
		self.basedir = os.path.abspath(os.path.dirname(__file__))
		self.interval = 1
		self.recursive = True
		self.observedExts = []
		self.observedItems = []

	def getFileList(self):
		# return file list of base directory
		fileList = []
		if self.recursive:
			for (root, dirs, files) in os.walk(self.basedir):
				for f in files:
					fileList.append(os.path.join(root, f))
		else:
			fileList = os.listdir(self.basedir)

		# extention filtering (option)
		if len(self.observedExts) > 0:
			fileList_cpy = list(fileList)
			for f in fileList_cpy:
				if not getExt(f) in self.observedExts:
					fileList.remove(f)

		return fileList

	def checkDir(self, recursive=True):
		# get file list
		fileList = self.getFileList()
		# get observed item list now
		items = [ObservedItem(f) for f in fileList]
		# create list for detecting items deleted
		deletedItems = list(self.observedItems)
		for item in items:
			if item in self.observedItems:
				# check the time-stamps
				idx = self.observedItems.index(item)
				if self.observedItems[idx].isModified(item):
					self.observedItems.remove(item)
					self.observedItems.append(item)
					self.handler.on_modifyify(item)
				# remove exist file from deleted items list
				deletedItems.remove(item)
			else:
				# detect new file
				self.observedItems.append(item)
				for observedItem in self.observedItems:
					if observedItem.isMoved(item) and observedItem in deletedItems:
						# detect moved file
						deletedItems.remove(observedItem)
						self.observedItems.remove(observedItem)
						self.handler.on_move(item)
						break
				else:
					self.handler.on_add(item)
		# detect deleted file
		for item in deletedItems:
			self.observedItems.remove(item)
			self.handler.on_delete(item)

	def setSchedule(self, 
					handler,
					interval=1, 
					directory=os.path.abspath(os.path.dirname(__file__)),
					recursive=True):
		# set Wathing schedule
		self.handler = handler
		self.interval = interval
		self.basedir = directory
		self.recursive = recursive

	def run(self):
		# run observeding thread
		if self.handler is None:
			sys.stderr.write("[ERROR]: you must set any event handler")
			return
		while not self.stop_event.is_set():
			self.checkDir(self.recursive)
			time.sleep(self.interval)

	def stop(self):
		# stop observeding thread
		self.stop_event.set()
		self.join()