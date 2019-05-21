'''
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
'''

from itertools import combinations

rates1 = [[1, 2, 4, 0.5], [0.5, 1, 100, 1], [.25, .01, 1, 1], [2, 1, 1, 1]]
rates2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def prod_list(arr):
    running = 1
    for x in arr:
        running *= x
    return running

def day32(rates):
    input = [x[0] for x in rates]
    output = sum([map(list, combinations(input, i)) for i in range(len(input) + 1)], [])
    for possibility in output:
        if (prod_list(possibility)) > 1:
            return True
    return False

print(day32(rates1))
print(day32(rates2))
