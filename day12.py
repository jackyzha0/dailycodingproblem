'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
'''

def stepcomb(n):
    a, b = 1, 2
    for _ in range(n - 1):
        c = b
        b = a + b
        a = c
    return a

print(stepcomb(4))
