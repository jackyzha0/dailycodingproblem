'''
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

test = [[5, 2, 1],
        [3, 1, 1],
        [10, 9, 3]] # should return 5 (3 + 1 + 1)

def d19(arr):
    p_ind = arr[0].index(min(arr[0]))
    cost = arr[0][p_ind]
    for n in arr[1:]:
        n.pop(p_ind)
        cost += min(n)
        p_ind = n.index(min(n))

    return cost

print(d19(test))
