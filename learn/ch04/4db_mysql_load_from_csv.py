#!/usr/bin/env python3
import sys

import pymysql

input_file = sys.argv[1]
con = pymysql.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='my_password')
c = con.cursor()
