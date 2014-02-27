#!/usr/bin/env python
# Author: Sam Wilkins
# CIS3760

import sys
import xlrd
import json

if len(sys.argv) < 2:
	sys.exit('No input file')

filename = sys.argv[1]

HDI_book = xlrd.open_workbook(filename = filename)

HDI_sheet = HDI_book.sheet_by_name('anonymized data')

rows = list()
head_row = HDI_sheet.row(0)
head_values = [cell.value for cell in head_row]

for row_index in xrange(1, HDI_sheet.nrows):
	row = HDI_sheet.row(row_index)
	values = [cell.value for cell in row]
	row_dict = dict(zip(head_values, values))
	rows.append(row_dict)

json_string = '{\n"CFS_Reports": ' + json.dumps(rows, indent = 0) + '\n}'
print json_string
