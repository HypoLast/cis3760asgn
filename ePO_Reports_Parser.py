#!/usr/bin/env python

#Author: Justin Gruber

import sys
import csv
import json
import os
import time
import collections

def parseEPO():
	#Initializing base variables
	rowCount = 0
	argCount = 0
	jsonString = ("{'apikey' : 'b980d57f35d0dcc8508fcfb02ae27db3ffc6e5ed',\n"
				"'datavault': 'ePO_Reports', \n" 
				"'timestamp':'")
	jsonString += str(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(time.time()))) 
	jsonString += "',\n'data' : [\n"

	#Checking arguement(s)
	for arg in sys.argv:
		if argCount == 0:
			argCount += 1
		elif not str(arg).lower().endswith(".csv"):
			sys.stderr.write("Error: File given must be of csv format.\n")
			sys.exit()
		else:
			fileName = str(arg)

	#Getting the length of the file for when commas are being added in the list
	fileLen = len(open(fileName, "r").readlines())
	if fileLen == 0:
		sys.stderr.write("Error: File has no content")
		sys.exit()

	#Opening file for reading
	epoFile = open(fileName, "r")

	#Reading the first line of the file to get the column names
	colNames = csv.reader(epoFile, delimiter=',')
	headings = colNames.next()

	#Getting all of the information from the file into a dictionary using
	#the column names as keys
	information = csv.DictReader(epoFile, headings, delimiter=',')
	for row in information:
		row = collections.OrderedDict(sorted(row.items()))
		jsonString += json.dumps(row)
		rowCount += 1
		if rowCount == (fileLen - 1):
			jsonString += "\n"
		else:
			jsonString += ",\n"

	jsonString += "]}"

	#print jsonString
	return jsonString


print parseEPO()