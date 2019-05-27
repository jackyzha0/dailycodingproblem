'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for r in range(len(matrix[0])):
            t = []
            for c in range(len(matrix)):
                t.append(matrix[c][r])

            matrix[0][r] = t[::-1]

        for r in range(len(matrix[0])):
            matrix[len(matrix) - 1 - r] = matrix[0][len(matrix) - 1 -r]

#Top 99.31% runtime
