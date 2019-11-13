'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

inp = [3, 4, -1, 1]
inp = [1, 2, 0]

# O(n) time O(n) space solution

def firstposint(inp):
    m = max(inp)
    z_arr = ['-'] * m
    for x in inp:
        if x > 0:
            z_arr[x-1] = 'x'

    print(z_arr)

    try:
        return z_arr.index('-') + 1
    except:
        return m + 1

print(firstposint(inp))

# O(n) time O(1) space solution

def firstposint1(inp):
    m = max(inp)
    inp = [x if x > 0 else 0 for x in inp]
    for x in inp:
        inp[abs(x)-1] = -1 * abs(inp[abs(x)-1])

    print(inp)
    for x in range(m):
        if inp[x] > 0:
            return x + 1
    return m + 1

print(firstposint1(inp))
