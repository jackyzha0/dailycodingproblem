'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def longestSub(s, k):
    #pointer 1
    #pointer 2
    #longest
    #set

    #if pointer1 == pointer2
    #pointer2++ until pointer1 != pointer2

    #add all characters in between pointer1 and pointer2 to set
    #pointer 2++
    #if pointer2 in set
    #pointer1++

    #if valid and longest, update longest
    #return length of longest

    p1 = 0
    p2 = 0
    longest = ""
    nset = set()

    while s[p1] == s[p2]:
        p2 += 1

    print(p1, p2)

inp = "abcda"
k = 2

print(longestSub(inp, k))
