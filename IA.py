import flip as ff
import movement as mm
import boardPoints as bp

# testing boards
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
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 2, 1, 0, 0, 0,
      0, 0, 0, 1, 2, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]

# examine changes by a tile
# update points
# returns users points and enemys points

alpha0 = -1000000
beta0 = 1000000


def getScore(board, turn, tile, points):
    tempBoard = ff.flipAll(board, turn, tile)
    # mm.printBoard(tempBoard)
    points = bp.updatePoints(board, points, turn)
    mine, opp = bp.countPoints(tempBoard, turn, points)
    return mine, opp, tempBoard

# gets all the points for each posible movement in a board


def getAllScores(board, turn, points):
    myPoints = []
    opponentP = []
    a = mm.analize(board, turn, False, True)
    for i in a:
        scores = getScore(board, turn, i, points)
        myPoints.append(scores[0])
        opponentP.append(scores[1])
    return a, myPoints, opponentP


def corners(movesArray):
    if 0 in movesArray:
        return 0
    elif 7 in movesArray:
        return 7
    elif 56 in movesArray:
        return 56
    elif 63 in movesArray:
        return 63
    else:
        return False


# minimax w/ alpha beta prunning


def minimax(board, turn, points, depth, isMaximizing, alpha, beta):
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

# simple chooser


def getBest(board, turn, points):
    moves, myPoints, opp = getAllScores(board, turn, points)
    corner = corners(moves)
    if corner != False:
        return corner
    maximo = myPoints.index(max(myPoints))
    return moves[maximo]
