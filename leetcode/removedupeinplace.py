# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.

def soln(arr):
    res = 0

    if arr:
        for i in range(len(arr) - 1):
            if not arr[i] == arr[i + 1]:
                res += 1

        return res + 1
    return 0

assert soln([1,1,2]) == 2
assert soln([0,0,1,1,1,2,2,3,3,4]) == 5
assert soln([0,1]) == 2
assert soln([0]) == 1
assert soln([0, 0]) == 1
assert soln([]) == 0
