'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

def day69(arr):
    s = sorted(arr)
    pos = [x for x in s if x > 0]
    neg = [abs(x) for x in s if x < 0]

    s3 = pos[-3:]
    twon = neg[:2] + [pos[-1]]

    res = max(pos[-3:], neg[:2] + [pos[-1]])
    r = 1

    for i in res:
        r *= i

    return r

ex1 = [-10, -10, 5, 2, 1]
print(day69(ex1))
