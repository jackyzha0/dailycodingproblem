'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time
def sched(f, n):
    time.sleep(n/1000.)
    return f

def test(n1, n2):
    return n1 + n2

print(int(round(time.time() * 1000)))
print(sched(test(1, 2), 5))
print(int(round(time.time() * 1000)))
