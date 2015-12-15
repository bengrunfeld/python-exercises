#! /usr/env python

menu = {}
blends = ('lovo', 'anduino', 'especiale')
coffee_types = [x.upper() for x in blends if len(x) > 4]

def write_menu(coffee_list):
    for i, coffee in enumerate(coffee_list):
        menu[coffee] = "{}.{} is a medium roast".format(i, coffee)    
write_menu(coffee_types)

print 'DICTIONARY OF COFFEE'
print '---------------'
print menu



 
