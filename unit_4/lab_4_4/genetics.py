#! /usr/bin/env python

proteins = {'GCA': 'stable', 'TGC': 'stable', 'TGC': 'stable', 'GAA': 'volatile', 'ACT': 'stable', 'TTG': 'stable', 'GCT': 'stable'}

if 'GAA' in proteins:
    del proteins['GAA']

print proteins
