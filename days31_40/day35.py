'''
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def day35_meme(arr):
    l = len(arr)
    arr[-3] = arr.count('R')
    arr[-2] = arr.count('G')
    arr[-1] = l - (arr[-3] + arr[-2])

    arr = 'R' * arr[-3] + 'G' * arr[-2] + 'B' * arr[-1]
    return arr

def swap(l, p1, p2):
    l[p1], l[p2] = l[p2],l[p1]
    return l



test = ['R']
print(day35(test))
