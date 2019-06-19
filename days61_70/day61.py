'''
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

def day61(x, n):
    res = 1
    while n > 0:
        if n % 2 != 0:
            res = res*x

        n = int(n/2)
        x = x*x

    return res

print(day61(5,5))
