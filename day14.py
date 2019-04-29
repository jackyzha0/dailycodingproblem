'''
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''


import math
import random

iters = 100000
inside = 0

for i in range(iters):
    x = random.random()**2
    y = random.random()**2
    if (x+y) < 1:
        inside += 1

pi = float(inside)/float(iters) *4

print(pi)
