#!/usr/bin/env python
# Author: Sam Wilkins
# CIS3760

import sys
import xlrd
import json
import time

def main():
	if len(sys.argv) < 2:
		sys.exit('No input file')

	filename = sys.argv[1]

	HDI_book = xlrd.open_workbook(filename = filename)
	result_dict = { 'tablename' : 'HDI_Reports',
					'timestamp' : time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(time.time()))
				  }
	rows = list()

	for sheet_index in xrange(0, HDI_book.nsheets):
		HDI_sheet = HDI_book.sheet_by_index(sheet_index)

		head_row = HDI_sheet.row(0)
		head_values = [cell.value for cell in head_row]

		for row_index in xrange(1, HDI_sheet.nrows):
			row = HDI_sheet.row(row_index)
			values = [cell.value for cell in row]
			row_dict = dict(zip(head_values, values))
			rows.append(row_dict)

	result_dict['data'] = rows
	json_string = json.dumps(result_dict, indent = 2)
	print json_string

if __name__ == '__main__':
	main()