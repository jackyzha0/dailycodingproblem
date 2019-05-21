'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

ex1 = "race"
ex2 = "google"

import math

def checkPalindrome(string):
    if len(string) % 2 == 0:
        i = len(string)/2
        return string[i:] == string[:i][::-1]
    else:
        i1 = int(math.floor(float(len(string))/2))
        i2 = int(math.ceil(float(len(string))/2))
        return string[i1:] == string[:i2][::-1]

def day34(string):
    i = len(string)
    append = string[::-1][:i]

    for x in range(1, i+1):
        append = string[::-1][:x]
        if checkPalindrome(append + string):
            return append + string
        
print(day34(ex1))
print(day34(ex2))
