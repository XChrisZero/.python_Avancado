# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step=8, start=8) # contador infinito
r1 = range(8, 100, 8) # iterador finito

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count') # cuidado com loops infinitos
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')

for i in r1: # cuidado com loops infinitos
    print(i)