#!/usr/bin/env python3
from numpy import dtype, loadtxt

person_dtype = dtype([('name', 'S10'), ('age', int), ('color', 'S6'), ('score', float)])
people = loadtxt('people.txt', skiprows=1, dtype=person_dtype)
print(people)
