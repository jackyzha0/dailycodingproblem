'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
'''

def median(arr):
    n = len(arr)

    if n % 2 == 1:
        return arr[n//2]
    else:
        return sum(arr[n//2-1:n//2+1])/2.0

def day33(arr):
    res = []
    s = []
    for x in arr:
        s.append(x)
        s = sorted(s)
        print(median(s))


arr = [2, 1, 5, 7, 2, 0, 5]
day33(arr)
