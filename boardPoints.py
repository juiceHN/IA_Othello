import reversi
import movement as mm
b1 = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 2, 1, 0, 0, 0,
      0, 0, 0, 1, 2, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]


def initial():
    points = [1000, -50, 0, 0, 0, 0, -50, 1000,
              -50, -50, 10, 10, 10, 10, -50, -50,
              0, 10, 50, 50, 50, 50, 10, 0,
              0, 10, 50, 50, 50, 50, 10, 0,
              0, 10, 50, 50, 50, 50, 10, 0,
              0, 10, 50, 50, 50, 50, 10, 0,
              -50, -50, 10, 10, 10, 10, -50, -50,
              1000, -50, 0, 0, 0, 0, -50, 1000]
    return points


def initialL(points):
    update = [16, 24, 32, 40]
    for i in update:
        points[i] = 70
    update = [17, 25, 33, 41]
    for i in update:
        points[i] = 50
    return points


def initialR(points):
    update = [23, 31, 39, 47]
    for i in update:
        points[i] = 70
    update = [22, 30, 38, 46]
    for i in update:
        points[i] = 50
    return points


def initialU(points):
    update = [2, 3, 4, 5]
    for i in update:
        points[i] = 70
    update = [10, 11, 12, 13]
    for i in update:
        points[i] = 50
    return points


def initialD(points):
    update = [58, 59, 60, 61]
    for i in update:
        points[i] = 70
    update = [50, 51, 52, 53]
    for i in update:
        points[i] = 50
    return points


def corner1(points):
    points[8] = 70
    points[1] = 70
    points[9] = 50
    return points


def corner2(points):
    points[6] = 70
    points[15] = 70
    points[14] = 50
    return points


def corner3(points):
    points[48] = 70
    points[57] = 70
    points[49] = 50
    return points


def corner4(points):
    points[55] = 70
    points[62] = 70
    points[54] = 50
    return points


def corner12(points):
    points[8] = -20
    points[1] = -20
    points[9] = -20
    return points


def corner22(points):
    points[6] = -20
    points[15] = -20
    points[14] = -20
    return points


def corner32(points):
    points[48] = -20
    points[57] = -20
    points[49] = -20
    return points


def corner42(points):
    points[55] = -20
    points[62] = -20
    points[54] = -20
    return points


def updatePoints(board, points, turn):
    op = mm.getOposition(turn)
    for i in range(len(board)):
        if i >= 10 and i < 14:
            if board[i] != 0:
                points = initialU(points)
        if i >= 50 and i < 54:
            if board[i] != 0:
                points = initialD(points)
        if i in [17, 25, 33, 41]:
            if board[i] != 0:
                points = initialL(points)
        if i in [22, 30, 38, 46]:
            if board[i] != 0:
                points = initialR(points)
        if board[0] == turn:
            points = corner1(points)
        if board[7] == turn:
            points = corner2(points)
        if board[56] == turn:
            points = corner3(points)
        if board[63] == turn:
            points = corner4(points)
        if board[0] == op:
            points = corner12(points)
        if board[7] == op:
            points = corner22(points)
        if board[56] == op:
            points = corner32(points)
        if board[63] == op:
            points = corner42(points)
    points = strat(board, turn, points)
    return points

border = [2, 3, 4, 5, 16, 24, 32, 40, 23, 31, 39, 47, 58, 59, 60, 61]
border2 = [[2, 3, 4, 5], [16, 24, 32, 40], [23, 31, 39, 47], [58, 59, 60, 61]]


def strat(board, turn, points):
    opposite = mm.getOposition(turn)
    for i in range(len(board)):
        if i in border:
            if i in border2[0]:
                if board[i] == opposite:
                    if board[i + 1] == 0:
                        points[i + 1] += -30
                    if board[i - 1] == 0:
                        points[i - 1] += -30
                    if board[i + 2] == 0:
                        points[i + 2] += 20
                    if board[i - 2] == 0:
                        points[i - 2] += 20
            elif i in border2[1]:
                if board[i] == opposite:
                    if board[i + 8] == 0:
                        points[i + 8] += -30
                    if board[i - 8] == 0:
                        points[i - 8] += -30
                    if board[i + 16] == 0:
                        points[i + 16] += 20
                    if board[i - 16] == 0:
                        points[i - 16] += 20
            elif i in border2[2]:
                if board[i] == opposite:
                    if board[i + 8] == 0:
                        points[i + 8] += -30
                    if board[i - 8] == 0:
                        points[i - 8] += -20
                    if board[i + 16] == 0:
                        points[i + 16] += 20
                    if board[i - 16] == 0:
                        points[i - 16] += 20
            elif i in border2[3]:
                if board[i] == opposite:
                    if board[i + 1] == 0:
                        points[i + 1] += -30
                    if board[i - 1] == 0:
                        points[i - 1] += -30
                    if board[i + 2] == 0:
                        points[i + 2] += 20
                    if board[i - 2] == 0:
                        points[i - 2] += 20
    return points


def countPoints(board, turn, points):
    opposite = mm.getOposition(turn)
    my, op = 0, 0
    for i in range(len(board)):
        if board[i] == turn:
            my += points[i]
        elif board[i] == opposite:
            op += points[i]
    return my, op
'''
a = initial()
reversi.printBoard2(a)
a = strat(b1, 1, a)
reversi.printBoard2(a)
print(countPoints(b1, 1, a))
a = updatep(b1, a, 1)
reversi.printBoard2(a)
countPoints(b1, 1,a)
'''
