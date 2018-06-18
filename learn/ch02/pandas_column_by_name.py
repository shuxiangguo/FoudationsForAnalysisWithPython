#!/usr/bin/env python3
import sys

import pandas as pd

input_file = sys[1]
output_file = sys[2]
data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)
