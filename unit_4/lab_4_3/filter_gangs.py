#! /usr/bin/env python

bad_a_listers = ['Sean Connery', 'Matt Damon', 'Christina Aguilera', 'Brad Pitt', 'Liam Neeson']

bad_b_listers = ['Rick Moranis', 'Matt Damon', 'Bruce Campbell', 'Brad Pitt', 'Pierce Brosnan']

a_set = set(bad_a_listers)
b_set = set(bad_b_listers)

members_of_both = a_set & b_set

for member in members_of_both:
    print "{} is a member of both gangs".format(member)

