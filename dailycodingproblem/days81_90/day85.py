'''
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
'''

x = int('10001', 2)
y = int('10101', 2)
b = int('00000', 2)

def strfmt(n):
    return "{0:b}".format(n)

print(strfmt((x & b) | (y & ~b)))
