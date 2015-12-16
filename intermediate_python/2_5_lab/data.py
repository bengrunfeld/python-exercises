#! /usr/bin/env python
data = [ 
  [53, 64, 28, 99],
  [93, 16, 42, 33],
  [85, 75, 29, 42],
  [47, 59, 13, 21],
  [34, 53, 12, 14],
  [15, 34, 31, 78],
  [86, 57, 64, 61],
  [41, 26, 35, 58],
] 

# 1. Map the values to a named tuple 

dims = []

print '\n1.1 Print out all of the dimensions'
print dims 

print '\n1.2 Print out all of the widths'
for dim in dims:
  # code goes here

# 2. Use the widths as a key, and place all of the named tuples into an OrderedDict 
# Then print the value of the OrderedDict field which has a key of 42

print '\n2. An ordereddict of all the Dimensions'

print od[42]
