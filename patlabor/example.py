#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import shutil
import patlabor

class ExampleHandler(patlabor.FileEventHandler):
	def on_add(self, item):
		print "added"

	def on_modify(self, item):
		print "modified"

	def on_move(self, item):
		print "moved"

	def on_delete(self, item):
		print "deleted"

def main():
	here = os.path.abspath(os.path.dirname(__file__)) 
	handler = ExampleHandler()
	observer = patlabor.FileObserver()
	observer.observedExts.append('.txt')
	observer.setSchedule(handler=handler,
						 interval=1,
						 directory=here,
						 recursive=True)
	observer.start()
	# create .txt files!
	f = open("hoge.txt", "w")
	time.sleep(2)
	# modify .txt file
	f.write("hello patlabor-python!")
	f.close()
	time.sleep(2)	
	# move .txt file
	os.mkdir("sample")
	shutil.move("./hoge.txt", "sample/")
	time.sleep(2)
	# delete .txt file
	os.remove("sample/hoge.txt")
	os.rmdir("sample")
	observer.stop()		

if __name__ == '__main__':
	main()