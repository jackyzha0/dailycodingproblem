'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
'''

def safe_val_fetch(x, y, arr):
    if x < len(arr[0]) and y < len(arr):
        return arr[y][x]
    return -1

def gen_square(arr,x,y):
    filters = [(1, 1), (1, 0), (1, -1), (0, 1), (0, 1), (-1, 1), (-1, 0), (-1, 1)]
    vals = []
    for f in filters:
        r = safe_val_fetch(x + f[0], y + f[1], arr)
        if not r == -1:
            vals.append(r)

    return sum(vals) / len(vals)

def soln(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            arr[x][y] = gen_square(arr, x, y)

    return arr


arr = [[1,1,1],[1,0,1],[1,1,1]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
print(soln(arr))
print(soln(arr2))
