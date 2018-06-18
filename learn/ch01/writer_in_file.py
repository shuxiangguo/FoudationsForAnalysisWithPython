# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:12:01 2018

@author: shuxiangguo
"""

#write in a text file

import sys
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value] + '\t')
    else:
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()