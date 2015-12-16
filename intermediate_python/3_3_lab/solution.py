#! /usr/bin/env python

weight = [5, 10, 15, 20]
speed = [15, 20, 25, 30]


# 1. Perform a damage calculation on corresponding
# items from the 2 lists. The formula to calculate damage
# is x * (y / 2 * 100) + 50

def calculate_impact(x, y):
  return x * (y / 2 * 100) + 50

result = map(calculate_impact, weight, speed) 
print result

# 2. Remove any item from the list that isn't a multiple
# of 10

def multiple_of_ten(x):
  return x % 10 == 0

result = filter(multiple_of_ten, weight)
print result

# 3. Append the list of weights to the list of speeds 
# then use a reduce function to determine the largest
# number there 

speed.extend(weight)

def greater_than(x, y):
  if x > y:
    return x
  else:
    return y

result = reduce(greater_than, speed)
print result

