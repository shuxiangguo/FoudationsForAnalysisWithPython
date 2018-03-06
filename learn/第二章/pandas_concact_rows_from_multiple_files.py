#!/usr/bin/env python3
import glob
import os
import sys
import pandas as pd

input_path = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)
data_frame_concact = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concact.to_csv(output_file, index=False)