import random as rd


def allowedMoves(board):
    moves = []
    for i in range (board.size):
        for j in range(board.size):
            if (board.mat[i][j] == 0):
                moves.append((i,j))
    return moves

def randomGame(board, player):
    p = board.deepcopy()
    moves = allowedMoves(p)
    rd.shuffle(moves)
    j = player
    for elt in moves:
        p.play(elt, j)
        j = 3 - j
    if p.checkVictoire(player):
        return 1
    else:
        return 0

def boardScore(board, player, n):
    nbWon = 0
    for _ in range(n):
        nbWon += randomGame(board, player)
    return nbWon/n
        