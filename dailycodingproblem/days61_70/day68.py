'''
On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
'''

def checkdiags(board, m, x, y):
    c = 0
    #top left
    directions = []
    directions.append(zip(range(x + 1, m), range(y + 1, m)))
    directions.append(zip(range(x + 1, m), range(y - 1, -1, -1)))
    directions.append(zip(range(x - 1, -1, -1), range(y + 1, m)))
    directions.append(zip(range(x - 1, -1, -1), range(y - 1, -1, -1)))

    for _ in directions:
        for coord in _:
            if board[coord[0]][coord[1]] == 1:
                c += 1

    return c

def day68(m, bishops):
    count = 0
    board = [[0 for x in range(m)] for y in range(m)]

    for n in range(len(bishops)):
        board[bishops[n][0]][bishops[n][1]] = 1

    for n in range(len(bishops)):
        x, y = bishops[n][0], bishops[n][1]
        count += checkdiags(board, m, x, y)

    for row in board:
        print row

    return count/2

bishops = [(0,0),(1,2),(2,2),(4,0)]
#bishops = [(1,2)]
print(day68(5, bishops))
