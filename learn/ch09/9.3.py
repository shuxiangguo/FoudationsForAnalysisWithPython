#!/usr/bin/env python3
from numpy import genfromtxt

name_to_int = dict(rachel=1, john=2, clint=3)
color_to_int = dict(blue=1, green=2, red=3)


def convert_name(n):
    return name_to_int.get(n, -999)


def convert_color(n):
    return color_to_int.get(n, -999)


data = genfromtxt('people.txt', dtype=float, names=True, converters={0: convert_name, 2: convert_color})
print(data)
