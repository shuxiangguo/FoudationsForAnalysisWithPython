# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:56:31 2018

@author: shuxiangguo
"""
# usr/bin/env python3
import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']
                                                   .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)