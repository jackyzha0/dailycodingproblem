'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

def day40(arr):
    d = dict()

    for n in arr:
        if n not in d.keys():
            d[n] = 1
        else:
            d[n] += 1

    for k in d.keys():
        if d[k] == 1:
            return k

a = [6, 1, 3, 3, 3, 6, 6]
print(day40(a))
