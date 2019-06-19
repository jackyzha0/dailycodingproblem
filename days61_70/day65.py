'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

def day65(matrix):
    a = []
    res = []

    try:
        while True:
            app, matrix = removeRow(matrix)
            a.extend(app)
            matrix = rotateMat(matrix)
            res.append(matrix)
    except:
        return a

def removeRow(matrix):
    return matrix[0], matrix[1:]

def rotateMat(matrix):
    return list(zip(*matrix)[::-1])

ex1 = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
print(day65(ex1))
