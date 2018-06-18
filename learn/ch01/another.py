# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:08:06 2018

@author: shuxiangguo
"""
import glob
import os
import sys

#读取多个文件，并打印输出每行信息
print("Output #:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))