#!/usr/bin/env python
#Author: Erica Pisani

import collections
import json
import csv
import time

def parseFile(fileNameToParse):

	# Used to skip the first row in the file when parsing
	# for the information
	rowCount = 0
	jsonString = ("{'apikey' : 'b980d57f35d0dcc8508fcfb02ae27db3ffc6e5ed',\n"
				"'datavault': 'SCCM_SCEP_Reports', \n" 
				"'timestamp':'")
	jsonString += str(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(time.time()))) 
	jsonString += "',\n'data' : [\n"

	# Opening in universal newline mode. Ensures backward
	# compatibility.
	fileHandle = open(fileNameToParse, "U")

	fileLen = len(open(fileNameToParse, "r").readlines())

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
