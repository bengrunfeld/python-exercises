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

from collections import namedtuple

dims = []

Dimensions = namedtuple('Dimensions', ['weight', 'height', 'width', 'length']) 

for d in data:
  dims.append(Dimensions._make(d))
  
print '\n1.1 Count of the total votes'
print dims 

print '\n1.2 Print out all of the widths'
for dim in dims:
  print dim.width


# 2. Use the widths as a key, and place all of the named tuples into an OrderedDict 
# Then print the value of the OrderedDict field which has a key of 42

print '\n2. An ordereddict of all the Dimensions'

from collections import OrderedDict

od = OrderedDict()

for dim in dims:
  od[dim.width] = dim
  
print od[42]
