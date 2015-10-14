#! /usr/bin/env python

a = ['mouse', 'yarn', 'catgrass', 'string', 'foam ball', 'scratching post', 'ice cubes', 'water fosset', 'curtains']
b = []

print 'ORIGINAL CAT TOY LIST'
print '-------------'
print a
print '\n'

for i in range(len(a)):
    if i % 3 == 0:
        if 'i' in a[i]:
            b.append(i)

for i in reversed(b):
    del a[i]

print 'EDITED CAT TOY LIST'
print '-------------'
print a
print '\n'
