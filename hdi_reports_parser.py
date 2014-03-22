#!/usr/bin/env python
# Author: Sam Wilkins
# CIS3760

import sys
import xlrd
import json
import time
import datetime

def main():
	if len(sys.argv) < 2:
		sys.exit('No input files')
	
	filenames = sys.argv[1::]

	for name in filenames:
		try:
			print parseHDI(name)
		except Exception as ex:
			sys.stderr.write('Could not read ' + name + ': ' + str(ex) + '\n')

def parseHDI(filename):
	HDI_book = xlrd.open_workbook(filename = filename)
	json_strings = list()

	for sheet_name in HDI_book.sheet_names():
			json_strings.append(parseSheet(HDI_book, sheet_name))

	return json_strings

def parseSheet(HDI_book, sheet_name):
	HDI_sheet = HDI_book.sheet_by_name(sheet_name)
	
	result_dict = { 'tablename' : 'HDI_Reports',
		'timestamp' : time.strftime('%Y:%m:%d %H:%M:%S',
									time.localtime(time.time()))
		}
	rows = list()

	head_row = HDI_sheet.row(0)
	head_values = [cell.value for cell in head_row]
	
	for row_index in xrange(1, HDI_sheet.nrows):
		row = HDI_sheet.row(row_index)
		# Need to do all this crap to output dates properly
		values = [cell.value
				  if cell.ctype is not xlrd.XL_CELL_DATE
				  else datetime.datetime(*xlrd.xldate_as_tuple(
															   cell.value, HDI_book.datemode)).strftime('%Y:%m:%d')
				  for cell in row]
		row_dict = dict(zip(head_values, values))
		rows.append(row_dict)
	
	result_dict['data'] = rows
	json_string = json.dumps(result_dict, indent = 2)
	return json_string

if __name__ == '__main__':
	main()