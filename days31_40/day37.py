'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

import itertools
s = [1, 2, 3, 4]

def day37(s):
    nset = []

    def recur(a, remaining):
        t = []
        if not remaining:
            return a

        t.append(recur(a, remaining[1:]))
        t.append(recur(a+[remaining[0]], remaining[1:]))

        return t

    for i in s:
        nset.append(recur([], s[1:]))
        nset.append(recur([s[0]], s[1:]))

    return nset[0:2]

print(day37(s))
