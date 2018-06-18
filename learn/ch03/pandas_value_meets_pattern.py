#!/usr/bin/env python3

import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_meets_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]
writer = pd.ExcelWriter(output_file)
data_frame_meets_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
