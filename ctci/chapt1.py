# 1.1 - check if all chars in string are unique
def allUnique(str):
    return list(set(str)) == list(str)


assert allUnique("asdf")
assert not allUnique("aab")

# 1.1 Follow Up - do it in O(1) space
def allUnique_f(str):
    while str:
        c = str[:1]
        str = str[1:]

        if c in str:
            return False
    return True


assert allUnique("asdf")
assert not allUnique("aab")

# 1.3 - remove duplicates of string in O(1) space
def removeDupesInString(str):
    res = ""
    while str:
        c = str[:1]
        str = str[1:]

        if c not in str:
            res += c

    return res


assert removeDupesInString("asdf") == "asdf"
assert removeDupesInString("aab") == "ab"

# 1.4 - check if strings are anagrams of each other
def checkAnagram(s1, s2):
    return set(s1) == set(s2)

assert not checkAnagram("abc","bc")
assert checkAnagram("abc","abc")
assert checkAnagram("abc","bca")

# 1.5 - replace all spaces with "%20"
def encodeURL(str):
    return str.replace(" ","%20")

assert encodeURL("abc") == "abc"
assert encodeURL("a b c ") == "a%20b%20c%20"

# 1.8

def isSubtring(s1, s2):
    # implementation given
    pass

def isRotation(s1, s2):
    return isSubtring(s1, s2*2) or isSubtring(s2, s1*2)
