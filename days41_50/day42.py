'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

def day42(s, k):
    kf = k
    s = sorted([x for x in s if x <= k])
    out = []

    while sum(out) != kf:
        if len(s) == 0:
            return None

        while s[-1] > k:
            s.pop()

        p = s.pop()
        k -= p
        out.append(p)

    return out

ex1 = [12, 1, 61, 5, 9, 2], 24
print(day42(ex1[0], ex1[1]))
