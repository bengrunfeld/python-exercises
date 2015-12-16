#! /usr/bin/env python
states = {
  'al': {'john': 10, 'paul': 18, 'george': 13, 'ringo': 2},
  'ak': {'john': 25, 'paul': 12, 'george': 22, 'ringo': 21},
  'az': {'john': 19, 'paul': 7, 'george': 12, 'ringo': 15},
  'ar': {'john': 22, 'paul': 16, 'george': 20, 'ringo': 18},
  'ca': {'john': 27, 'paul': 23, 'george': 17, 'ringo': 6},
} 

# 1. Count the total votes of each candidate
from collections import Counter

count = Counter()

for s in states.keys():
  for candidate in states[s].keys():
    count[candidate] += states[s][candidate] 

print '\n1. Count of the total votes'
print count 


# 2. Place the candidates in a deque, remove the first
# beatle from the left side of the dequq, then add Brian,
# the fifth Beatle, at the start of the deque 

from collections import deque

dq = deque()

for c in count:
  dq.append(c)

# Remove the first Beatle from the Deque
dq.popleft()

dq.appendleft('brian')


print '\n2. A deque of the new beatles group'
print dq

# 3. Use a DefaultDict to add each candidate and their
# scores, besides Brian. Then try to access Brian

from collections import defaultdict

dd = defaultdict(int)

for c in count:
  dd[c] = count[c] 

print dd['brian']

print '\n3. A defaultdict of the candidates plus their votes'
print dd

