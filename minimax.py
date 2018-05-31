import flip as ff
import movement as mm
import boardPoints as bp
import math
b1 = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 1, 1, 1, 0, 0,
      0, 0, 2, 1, 1, 1, 0, 0,
      0, 0, 2, 1, 1, 1, 0, 0,
      0, 2, 0, 2, 0, 0, 0, 0,
      0, 0, 0, 0, 2, 0, 0, 0]

b2 = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 2, 0, 0, 0, 0, 0,
      0, 0, 0, 1, 1, 0, 0, 0,
      0, 0, 0, 1, 2, 0, 0, 0,
      0, 0, 1, 0, 2, 0, 0, 0,
      0, 1, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]


def getScore(board, turn, tile, points):
    tempBoard = ff.flipAll(board, turn, tile)
    # mm.printBoard(tempBoard)
    points = bp.updatePoints(board, points, turn)
    mine, opp = bp.countPoints(tempBoard, turn, points)
    return mine, opp, tempBoard


def minimax(board, turn, points, depth, isMaximizing):
    # mm.analize(board)
    if depth == 0:
        score = bp.countPoints(board, turn, points)
        return score
    moves = mm.analize(board, turn)
    if isMaximizing:
        t1, t2 = [], []
        opp = mm.getOposition(turn)
        maxScore = -1000000
        for i in moves:
            newMaxScore, mover = minimax(ff.flipAll(
                board, turn, i), opp, points, depth - 1, False)
            t1.append(newMaxScore)
            t2.append(mover)
            maxScore = max(maxScore, newMaxScore)
        mymove = t1.index(maxScore)
        mymove = moves[mymove]
        return(maxScore, mymove)
    else:
        minScore = 1000000
        t3, t4 = [], []
        for i in moves:
            newMinScore, mover = minimax(ff.flipAll(
                board, turn, i), turn, points, depth - 1, True)
            t3.append(newMinScore)
            t4.append(mover)
            minScore = min(minScore, newMinScore)
        mymove = t3.index(minScore)
        mymove = moves[mymove]
        return(minScore, mymove)


def minimax2(board, turn, points, depth, isMaximizing, alpha, beta):
    moves = mm.analize(board, turn)
    if depth == 0 or len(moves) == 0:
        score = bp.countPoints(board, turn, points)
        return score
    if isMaximizing:
        t1, t2 = [], []
        opp = mm.getOposition(turn)
        maxScore = -math.inf
        for i in moves:
            newBoard = ff.flipAll(board, turn, i)
            newMaxScore, mover = minimax2(
                newBoard, opp, points, depth - 1, False, alpha, beta)
            t1.append(newMaxScore)
            t2.append(mover)
            maxScore = max(maxScore, newMaxScore)
            alpha = max(alpha, maxScore)
            if beta <= alpha:
                break
        mymove = t1.index(maxScore)
        mymove = moves[mymove]
        return(maxScore, mymove)
    else:
        minScore = math.inf
        t3, t4 = [], []
        for i in moves:
            newBoard = ff.flipAll(board, turn, i)
            newMinScore, mover = minimax2(
                newBoard, turn, points, depth - 1, True, alpha, beta)
            t3.append(newMinScore)
            t4.append(mover)
            minScore = min(minScore, newMinScore)
            beta = min(beta, minScore)
            if beta <= alpha:
                break
        mymove = t3.index(minScore)
        mymove = moves[mymove]
        return(minScore, mymove)

'''
a = mm.analize(b2, 1, False, True)
print(a)
points = bp.initial()
w = minimax2(b2, 1, points, 3, True)
a = mm.analize(b2, 1, False, True)
print(a)
print (w)
'''
