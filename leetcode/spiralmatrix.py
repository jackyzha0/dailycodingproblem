'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        a = []

        try:
            while True:
                app, matrix = self.removeRow(matrix)
                a.extend(app)
                matrix = self.rotateMat(matrix)
                print(matrix)
        except:
            return a

    def removeRow(self, matrix):
        return matrix[0], matrix[1:]

    def rotateMat(self, matrix):
        return list(zip(*matrix)[::-1])

#Top 99.05% runtime
