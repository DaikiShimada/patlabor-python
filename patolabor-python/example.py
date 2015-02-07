#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import patolabor-python as pp

class ExampleHandler(pp.FileEventHandler):
	def on_add(self, item):
		pass

	def on_modify(self, item):
		pass

	def on_move(self, item):
		pass

	def on_delete(self, item):
		pass

def main():
	here = os.path.abspath(os.path.dirname(__file__)) 
	handler = ExampleHandler()
	observer = pp.FileObserver()
	observer.observedExts.apped('.txt')
	observer.setSchedule(handler=handler,
						 interval=1,
						 directory=here,
						 recursive=True)
	observer.start()
	# create .txt files!
	f = open("hoge.txt", "w")
	time.sleep(2)
	# modify .txt file
	f.write("hello patolabor-python!")
	f.close()
	time.sleep(2)	
	# move .txt file
	os.mkdir("sample")
	shutil.move("./hoge.txt", "sample/")
	# delete .txt file
	os.remove("sample/hoge.txt")
	os.rmdir("sample")
	observer.stop()		

if __name__ == '__main__':
	main()