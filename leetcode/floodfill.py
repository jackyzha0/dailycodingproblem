#  An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.

# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        startPixelCol = image[sr][sc]

        if startPixelCol == newColor:
            return image

        def overwrite(y, x):
            # fill current pixel with newColor on im
            # check if pixels are valid (in bounds, same col as startPixel)
            # call overwrite on those coords

            image[y][x] = newColor

            if not y == 0 and (image[y-1][x] == startPixelCol):
                overwrite(y-1, x)
            if not y == (len(image) - 1) and (image[y+1][x] == startPixelCol):
                overwrite(y+1, x)
            if not x == 0 and (image[y][x-1] == startPixelCol):
                overwrite(y, x-1)
            if not x == (len(image[0]) - 1) and (image[y][x+1] == startPixelCol):
                overwrite(y, x+1)

        overwrite(sr, sc)

        return image

# Top 93.71% runtime

S = Solution()
assert S.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
