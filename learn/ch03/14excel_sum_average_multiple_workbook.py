#!/usr/bin/env python3
import sys

from xlwt import Workbook

input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_average')
all_data = []
sales_column_index = 3
header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average',
          'workbook_total', 'workbook_average']
