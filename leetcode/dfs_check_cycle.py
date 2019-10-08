'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
'''

# Check for loop using deep-first search

class graph():
    """
    Graph Node Class
    """
    def __init_(self, val, next = None):
        self.val = val
        self.next = next
        self.visited = False

    def visit(self):
        self.visited = True

def cons_graph(l):
    """
    Construct graph from list of elements in form (a,b) where
    the edge is directed from a -> b
    """
    
    pass

def soln(n, prereqs):
    g = cons_graph(prereqs)
