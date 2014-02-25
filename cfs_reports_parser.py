#!/usr/bin/env python

#Author: Justin Gruber

import sys
import csv
import json
import os

#Initializing base variables
rowCount = 0
argCount = 0
jsonString = "CFS_Reports: [\n"

#Checking arguement(s)
for arg in sys.argv:
	if argCount == 0:
		argCount += 1
		pass
	elif ".xls" not in str(arg):
		sys.stderr.write("Error: File given must be of xls format.\n")
		sys.exit()
	else:
		fileName = str(arg)

#Getting the length of the file for when commas are being added in list
fileLen = len(open(fileName, "rb").readlines())

#Opening the file provided
cfsFile = open(fileName, "rb")

#Reading the first line of the file to get the column names
colNames = csv.reader(cfsFile, delimiter='\t')
for row in colNames:
	headings = row
	break

#Getting all of the information from the file as a dictionary using
#the column names as keys
information = csv.DictReader(cfsFile, headings, delimiter='\t')
for row in information:
	if rowCount == 0:
		rowCount += 1
		pass
	else:
		jsonString += json.dumps(row) 
		rowCount += 1
		if rowCount == (fileLen - 1):
			jsonString += "\n"
		else:
			jsonString += ",\n"

jsonString += "]"

print jsonString