'''
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
'''

def day60(arr):
    arr.sort()
    s = sum(arr)/2

    #greedy solution
    i = 0
    f = 0
    for i in range(len(arr)):
        if sum(arr[0:i]) == s:
            f = i

    if f != 0 and sum(arr[f:]) == s:
        return True

    #edge case
    for x in arr:
        if s - x in arr:
            return True
    return False

ex1 = [15, 5, 20, 10, 35, 15, 10]
ex2 = [15, 5, 20, 10, 35]
ex3 = [3, 1, 1, 2, 2, 1]
ex4 = [1, 3, 3, 1]

print(day60(ex1))
print(day60(ex2))
print(day60(ex3))
print(day60(ex4))
