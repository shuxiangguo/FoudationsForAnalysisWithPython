# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:10:03 2018

@author: shuxiangguo
"""

#!usr/bin/env python3
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)