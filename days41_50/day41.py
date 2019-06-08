'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

def day41(arr, starting):
    #use key to find all vals
    #if none, return null
    #sort() and pick first
    #remove element, call recursively

    res = [x for x in arr if x[0] == starting]

    if len(res) == 0:
        return None
    else:
        res.sort()
        el = res[0]

        n_arr = [x for x in arr if x != el]

        it = [el[0]]


        if len(n_arr) == 0:
            it.extend([el[1]])
        else:
            it.extend(day41(n_arr, el[1]))

    return it

ex1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'
ex2 = [('SFO', 'COM'), ('COM', 'YYZ')]
ex3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'

print(day41(ex1[0], ex1[1]))
print(day41(ex3[0], ex3[1]))
