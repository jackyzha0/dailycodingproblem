'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

input = [10,15,3,7]
k = 17

def sum_in_arr(input, k):
    for x in input:
        if k - x in input:
            return True
    return False

print(sum_in_arr(input,k))
