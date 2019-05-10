'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def day25(string, regex):
    si = 0
    ri = 0

    while si < len(string):
        if string[si] != regex[ri] and regex[ri] != ".":
            return False
        else:
            si += 1
            ri += 1
    return True

s1 = "ray"
r1 = "rab"

print(day25(s1,r1))
