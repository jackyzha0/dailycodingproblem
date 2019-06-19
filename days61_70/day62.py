'''
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def pascal(n):
    a = [1, 1]

    for _ in range(2, n):
        n = [1]
        for x in range(len(a)-1):
            n.append(a[x] + a[x+1])
        n.append(1)
        a = n

    return a

def day62(n):
    num = 2*n - 1
    return pascal(num)[n-1]

print(day62(5))
