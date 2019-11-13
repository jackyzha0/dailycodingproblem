'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

ex1 = [34, -50, 42, 14, -5, 86]
ex2 = [-5, -1, -8, -9]

def day49(arr):
    conc_m = arr[0]
    curr_m = arr[0]

    for i in range(1, len(arr)):
        curr_m = max(arr[i], curr_m + arr[i])
        conc_m = max(conc_m, curr_m)

    return max(conc_m, 0)

print(day49(ex1))
print(day49(ex2))
