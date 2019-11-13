'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
import numpy as np
input = [1,2,3,4,5]

def getprod(arr):
    out = [1] * len(arr)
    for x in range(len(arr)):
        mask = [arr[x]] * len(arr)
        mask[x] = 1
        out = np.multiply(mask, out)
    return out

def getprod_withdiv(arr):
    prod = np.prod(arr)
    out = []
    for x in range(len(arr)):
        out.append(prod / arr[x])
    return out

print(getprod(input))
print(getprod_withdiv(input))
