# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:46:41 2018

@author: shuxiangguo
"""

#write into a csv file
import sys
my_numbers = [0,1,2,3,4,5,6,7,8,9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value]) + ',')
    else:
        filewriter.write(str(my_numbers[index_value]) + '\n')
filewriter.close()