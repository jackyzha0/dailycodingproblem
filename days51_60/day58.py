'''
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

def day58(arr, element):
    bin_ind = findmin_binary(arr, 0 , len(arr)-1)
    comb = arr[bin_ind:] + arr[:bin_ind]
    return binsearch(comb, 0, len(comb) - 1, element) + bin_ind

def findmin_binary(arr, bot, top):
    mid = int((bot + top)/2)

    if arr[mid] < arr[bot] and arr[mid] < arr[top]:
        return mid

    if arr[mid] > arr[bot] and arr[mid] > arr[top]:
        return mid + 1

    if arr[bot] > arr[mid]:
        v = findmin_binary(arr, bot, mid)

    return v

def binsearch(arr, low, high, val):
    if high < low:
        return None

    mid = int((low + high)/2)

    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        return binsearch(arr, mid, high, val)
    if arr[mid] > val:
        return binsearch(arr, low, mid, val)

arr = [13, 18, 25, 2, 8, 10]
element = 8

print(day58(arr, element))
