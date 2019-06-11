'''
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
'''

def day57(s, k):
    words = s.split(" ")
    res = []
    c = 0
    s = ""
    for i in range(len(words)):
        if c + len(words[i]) + 1 <= k:
            s += words[i] + " "
            c += len(words[i])
        else:
            res.append(s[:-1])
            c = len(words[i])
            s = words[i] + " "
    res.append(s[:-1])
    return res

s1, k1 = "the quick brown fox jumps over the lazy dog", 10
print(day57(s1, k1))
