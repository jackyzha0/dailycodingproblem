'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

string = "de"
set = ["dog", "deer", "deal"]

def naiveQuery(string, set):
    arr = []
    for x in set:
        if string in x:
            arr.append(x)

    return arr

print(naiveQuery(string, set))
