#!/usr/bin/env python

#Author: Justin Gruber

import sys
import csv
import json
import os
import collections

def parseCFS():
	#Initializing base variables
	rowCount = 0
	argCount = 0
	jsonString = "CFS_Reports: [\n"

	#Checking arguement(s)
	for arg in sys.argv:
		if argCount == 0:
			argCount += 1
		elif not str(arg).lower().endswith(".xls"):
			sys.stderr.write("Error: File given must be of xls format.\n")
			sys.exit()
		else:
			fileName = str(arg)

	#Getting the length of the file for when commas are being added in the list
	fileLen = len(open(fileName, "r").readlines())

	#Opening the file provided
	cfsFile = open(fileName, "r")

	#Reading the first line of the file to get the column names
	colNames = csv.reader(cfsFile, delimiter='\t')
	headings = colNames.next()

	#Getting all of the information from the file into a dictionary using
	#the column names as keys
	information = csv.DictReader(cfsFile, headings, delimiter='\t')
	for row in information:
		row = collections.OrderedDict(sorted(row.items()))
		jsonString += json.dumps(row) 
		rowCount += 1
		if rowCount == (fileLen - 1):
			jsonString += "\n"
		else:
			jsonString += ",\n"

	jsonString += "]"

	#print jsonString
	return jsonString

print parseCFS()