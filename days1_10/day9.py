'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

import sys
inp1 = [2,4,6,2,5] #13
inp2 = [5,1,1,5] #10
inp3 = [5,6,5] #10
inp4 = [5,1,5,1] #10
inp5 = [2,6,4,5,2] #11
inp6 = [1,2,5,2] #6

def largestnonconsec(nums):
    if len(nums) <= 2:
        return max(nums)
    else:
        excl = max(nums[0], 0)
        incl = max(nums[1], nums[1])

        for x in range(2, len(nums)):
            if excl > incl:
                new_e = excl
            else:
                new_e = incl

            incl = excl + nums[x]
            excl = new_e
        return max(excl, incl)       

print(largestnonconsec(inp1))
print(largestnonconsec(inp2))
print(largestnonconsec(inp3))
print(largestnonconsec(inp4))
print(largestnonconsec(inp5))
print(largestnonconsec(inp6))
