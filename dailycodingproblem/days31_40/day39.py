'''
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

import itertools

class grid():
    def pgrid(self):
        print('')
        for row in self.g:
            print(['*' if x == 1 else '.' for x in row])
        print('___')

    def __init__(self, live):
        self.x_max = max(sorted(live, key=lambda x: x[0]))[0]
        self.y_max = max(sorted(live, key=lambda x: x[1]))[1]
        self.g = [[0 for y in range(self.y_max + 1)] for x in range(self.x_max + 1)]

        self.setinits(live)

    def setinits(self, live):
        for coord in live:
            self.g[coord[0]][coord[1]] = 1

    def shiftgrid(self, dx, dy):

        if dx == 1:
            for r in range(self.x_max + 1):
                self.g[r] = [0] + self.g[r]
            self.x_max += 1
        elif dx == -1:
            for r in range(self.x_max + 1):
                self.g[r] = self.g[r] + [0]
            self.x_max += 1

        if dx != 0:
            newrow = [0 for y in range(self.y_max + 2)]
        else:
            newrow = [0 for y in range(self.y_max + 1)]
        if dy == 1:
            self.y_max += 1
            self.g.insert(0, newrow)
        elif dy == -1:
            self.y_max += 1
            self.g.append(newrow)

    def newcell(self, x, y):
        dx, dy = 0, 0
        if y > self.y_max:
            dy = -1
        elif y < 0:
            dy = 1

        if x > self.x_max:
            dx = -1
        elif x < 0:
            dx = 1

        self.shiftgrid(dx, dy)

        ddx, ddy = 0, 0
        if x < 0:
            ddx += 1
        if y < 0:
            ddy += 1

        self.g[x + ddx][y + ddy] = 1

    def getneighbours(self, x, y):
        n = list(itertools.product(range(x-1, x+2), range(y-1, y+2)))
        n.remove((x, y))

        neighbours = 0

        for coord in n:
            try:
                if coord[0] >= 0 and coord[1] >= 0 and self.g[coord[0]][coord[1]] == 1:
                    neighbours += 1
            except:
                pass

        return neighbours

    def step(self):
        for y in range(self.y_max + 1):
            for x in range(self.x_max + 1):
                n = self.getneighbours(x,y)

                if self.g[x][y] == 1:
                    if n < 2:
                        self.g[x][y] = 0
                    if n > 3:
                        self.g[x][y] = 0
                else:
                    if n == 3:
                        self.g[x][y] = 1

g = grid([[0,0],[3,2],[3,1]], 1)
g.pgrid()
g.step()
g.pgrid()
