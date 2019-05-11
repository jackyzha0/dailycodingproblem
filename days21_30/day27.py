'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def day27(string):
    popped = [string[0]]
    for c in string[1:]:
        if (c == ")" and popped[-1] == "(") or (c == "}" and popped[-1] == "{") or (c == "]" and popped[-1] == "["):
            popped.pop()
        else:
            popped.append(c)

    if popped:
        return False
    else:
        return True

s1 = "([])[]({})"
s2 = "([)]"
s3 = "((()"

print(day27(s2))
