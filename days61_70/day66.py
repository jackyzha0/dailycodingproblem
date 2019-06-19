'''
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

import random

def toss_biased():
    x = random.uniform(0.0, 1.0)

    if x >= 0.9:
        return 0.
    else:
        return 1.

#Using sample means as an unbiased estimator
def day66():
    n = 30
    sample_x = sum([toss_biased() for _ in range(n)])
    sample_y = sum([toss_biased() for _ in range(n)])

    if sample_x >= sample_y:
        return 0.
    else:
        return 1.

avg = sum([day66() for _ in range(1000)]) / 1000.
print(avg)

#Recursive Solution
def day66_recur():
    f1, f2 = toss_biased(), toss_biased()
    if f1 == f2:
        return day66_recur()
    elif f1 > f2:
        return 0
    else:
        return 1

avg = sum([day66_recur() for _ in range(1000)]) / 1000.
print(avg)
