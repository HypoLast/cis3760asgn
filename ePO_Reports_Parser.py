#!/usr/bin/env python

#Author: Justin Gruber
#Class: CIS * 3760

import sys
import csv
import json
import os

rowNum = 0

if len(sys.argv) != 2:
	sys.stderr.write("Error: Require 1 parameter")
else:
	if ".csv" not in str(sys.argv[1]):
		sys.stderr.write("Error: File provided is not a csv")
		sys.exit()

csvFile = open(sys.argv[1], 'rb')
#print os.path.basename(sys.argv[1]).strip(".csv")
#jsonFileName = sys.argv[1].strip(".csv") + ".json"
#jsonFile = open(jsonFileName, 'w')

headerReader = csv.reader(csvFile, delimiter=',', quotechar="|")
for row in headerReader:
	header = row
	break

rowCount = 0
infoReader = csv.DictReader(csvFile, header)
testStr = ""
testStr  = testStr + sys.argv[1] + ": [\n"
#jsonFile.write(sys.argv[1] + ": [\n")
for row in infoReader:
	if rowCount == 0:
		rowCount += 1
		pass
	else:
		testStr = testStr + json.dumps(row) + ",\n"
		#testStr = testStr + "\t" + str(json.dumps(row)) + "\n"
#		json.dump(row, jsonFile)
#		jsonFile.write(',\n')
#jsonFile.write("\n]")
testStr =  testStr + "]"

print testStr