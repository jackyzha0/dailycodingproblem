'''
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''

import random

def rand7():
    return random.randint(1,7)

def day71():
    res = rand7()
    if res > 5:
        return day71()
    else:
        return res

s = 0
for i in range(1000):
    s += (float(day71())/1000)

print(s)
