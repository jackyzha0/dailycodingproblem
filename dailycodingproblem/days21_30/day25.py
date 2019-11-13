'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def day25(string, regex):
    i = 0
    while i < len(string):
        if regex[i] not in [".","*"]:
            if regex[i] == string[i]:
                i += 1
            else:
                return False
        elif regex[i] == ".":
            i += 1
        else:
            print(day25(string[i:], regex[i:]))
            print(day25(string[i+1:], regex[i:]))
            print(day25(string[i:], regex[i+1:]))
            print(day25(string[i+1:], regex[i+1:]))
            return 0

    return True

s1 = "chat"
r1 = ".*at"

print(day25(s1,r1))
