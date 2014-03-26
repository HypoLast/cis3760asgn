#!/usr/bin/env python
#Author: Erica Pisani

import collections
import json
import csv
import time
import os
import sys

def parseMicrosoftAV():

	# Used to skip the first row in the file when parsing
	# for the information
	rowCount = 0
	argCount = 0
	fileName = None

	jsonString = ("{'apikey' : 'b980d57f35d0dcc8508fcfb02ae27db3ffc6e5ed',\n"
				"'datavault': 'SCCM_SCEP_Reports', \n" 
				"'timestamp':'")
	jsonString += str(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(time.time()))) 
	jsonString += "',\n'data' : [\n"


	#Checking arguement(s)
	print sys.argv

	for arg in sys.argv:
		if argCount == 0:
			argCount += 1
		elif not str(arg).lower().endswith(".csv"):
			sys.stderr.write("Error: File given must be of csv format.\n")
			sys.exit()
		else:
			fileName = str(arg)

	
	if (fileName is not None):
		fileLen = len(open(fileName, "r").readlines())
	else:
		sys.stderr.write("Error: No file was given\n")
		sys.exit()

	if fileLen == 0:
		sys.stderr.write("Error: File has no content")
		sys.exit()
	
	# Opening in universal newline mode. Ensures backward
	# compatibility.
	fileHandle = open(fileName, "U")


	colNames = csv.reader(fileHandle)
	headings = colNames.next()

	information = csv.DictReader(fileHandle, headings)
	for row in information:
		row = collections.OrderedDict(sorted(row.items()))
		jsonString += json.dumps(row)
		rowCount +=1
		if rowCount == (fileLen - 1):
			jsonString += "\n"
		else:
			jsonString += ",\n"

	jsonString += "]}"

	return jsonString

print parseMicrosoftAV()