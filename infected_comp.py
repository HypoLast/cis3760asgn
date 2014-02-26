#!/usr/bin/env python
#Author: Erica Pisani

import collections
import json
import csv

def parseThatShit(fileNameToParse):

	# Used to skip the first row in the file when parsing
	# for the information
	rowCount = 0

	jsonString = "AntiVirus_Reports: [\n"
	# Opening in universal newline mode. Ensures backward
	# compatibility.
	file = open(fileNameToParse, "U")

	fileLen = len(open(fileNameToParse, "r").readlines())

	colNames = csv.reader(file)
	headings = colNames.next()

	information = csv.DictReader(file, headings)
	for row in information:
		row = collections.OrderedDict(sorted(row.items()))
		jsonString += json.dumps(row)
		rowCount +=1
		if rowCount == (fileLen - 1):
			jsonString += "\n"
		else:
			jsonString += ",\n"

	jsonString += "]"

	print jsonString
	return jsonString
