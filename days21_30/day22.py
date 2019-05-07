'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

d1 = set(['quick', 'brown', 'the', 'fox'])
s1 = "thequickbrownfox"
d2 = set(['bed', 'bath', 'bedbath', 'and', 'beyond'])
s2 = "bedbathandbeyond"

def d22(dictionary, string):
    res = []
    
    p0 = 0
    p1 = 1

    while p1 < len(string) + 1:
        if string[p0:p1] in dictionary:
            res.append(string[p0:p1])
            p0 = p1
        p1 += 1

    return res

print(d22(d1, s1))
print(d22(d2, s2))
