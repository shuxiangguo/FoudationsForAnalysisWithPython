# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:04:02 2018

@author: shuxiangguo
"""


#读取一个文件，并打印输出每行信息
import sys
input_file = sys.argv[1]
print("Output ")
filereader = open(input_file, 'r')
for r in filereader:
    print(r.strip())
filereader.close()

