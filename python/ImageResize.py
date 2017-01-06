#! /usr/bin/env python
#-*- coding: utf-8 -*-
# @author: rechie
# 使用opencv修改图像大小

import cv2
import sys
import os
import getopt

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:],"i:",["help"])
		input_imagePath = ""
		for op,value in opts:
			if op == "-i":
				input_imagePath = value
			elif op == "--help":
				print "ImageResize.py -i <inputPath>"
				sys.exit()
		if input_imagePath:
			process(input_imagePath)
			print "Process sucessed!"
	except getopt.GetoptError:
		print "for help use --help"
		sys.exit()

def process(input_imagePath):
	filenumber = 0
	for file in os.listdir(input_imagePath):
		filenumber = filenumber + 1
		image_name = input_imagePath+file
		print str(filenumber)+'   '+image_name
		img = cv2.imread(image_name)
		while img.any():
			res = cv2.resize(img,(20,20),interpolation = cv2.INTER_CUBIC)
			cv2.imwrite(image_name,res)
			break

if __name__ == '__main__':
	main()
