'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

def day26(arr, k):
    i = 0
    end = False
    while not end:
        try:
            val = arr[i]
            i += 1
        except:
            return arr[i-k]

arr = [x for x in range(1000000)]
k = 50

print(day26(arr, k))
