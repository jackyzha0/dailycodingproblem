'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def encode(s):
    out = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
            if i == len(s) - 1:
                out += str(count)
                out += s[i-1]
                count = 1
        else:
            out += str(count)
            out += s[i-1]
            count = 1
    return out

def isnum(s):
    try:
        int(s)
        return True
    except:
        return False

def decode(s):
    string = ""
    p1 = 0
    p2 = 1

    while p2 < len(s) + 1:
        if isnum(s[p1:p2]):
            p2 += 1
        else:
            n = p2 - p1
            string += s[p1] * n
            p1 = p2
            p2 += 1
    return string

s = "AAAABBBCCDAA"
print(encode(s))
s2 = "4A3B2C1D2A"
print(decode(s))
