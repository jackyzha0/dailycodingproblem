'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def day70(n):
    n_ = 0
    num = 19
    while True:
        if sum([int(x) for x in list(str(num))]) == 10:
            n_ += 1
            if n == n_:
                return num
        num += 9

print(day70(2))
