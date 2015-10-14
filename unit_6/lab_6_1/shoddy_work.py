#! /usr/env python

menu = {}
blends = ('lovo', 'anduino', 'especiale')
coffee_types = [x.upper() for x in blends if len(x) > 4]

for i, coffee in enumerate(coffee_types):
    menu[coffee] = "{}:{} is a medium roast".format(i, coffee)    

print menu



 
