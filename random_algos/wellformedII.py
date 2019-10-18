# Check if a expression is wellformed with only the characters [,{,(,',],},)


def match(c1,c2):
    if c1 == "[" and c2 == "]":
        return True
    if c1 == "{" and c2 == "}":
        return True
    if c1 == "(" and c2 == ")":
        return True
    return False

def wellformed(s):
    stack = []
    open = ["(","[","{"]

    for c in s:
        if c in open:
            stack.append(c)
        else:
            val = stack.pop()
            if not match(val, c):
                return False
    return not stack

def wellformedII(s):
    stack = []
    open = ["(","[","{"]

    for c in s:
        if c in open:
            stack.append(c)
        else:
            if c == "'":
                if len(stack) > 0 and stack[-1] == "'":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                val = stack.pop()
                if not match(val, c):
                    return False
    return not stack

print(wellformedII("('')[()]"))
