import movement as mm
import copy
b1 = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 1, 1, 1, 0, 0,
      0, 0, 2, 1, 1, 1, 0, 0,
      0, 0, 2, 1, 1, 1, 0, 0,
      0, 0, 0, 2, 0, 0, 0, 0,
      0, 0, 0, 0, 2, 0, 0, 0]


def flipAll(board, turn, tile):
    newBoard = copy.copy(board)
    l = turnLeft(newBoard, turn, tile)
    r = turnRight(newBoard, turn, tile)
    u = turnUp(newBoard, turn, tile)
    d = turnDown(newBoard, turn, tile)
    ul = turnD1(newBoard, turn, tile)
    ur = turnD2(newBoard, turn, tile)
    dr = turnD3(newBoard, turn, tile)
    dl = turnD4(newBoard, turn, tile)
    if l != False:
        for i in l:
            newBoard[i] = turn
    if r != False:
        for i in r:
            newBoard[i] = turn
    if u != False:
        for i in u:
            newBoard[i] = turn
    if d != False:
        for i in d:
            newBoard[i] = turn
    if ul != False:
        for i in ul:
            newBoard[i] = turn
    if ur != False:
        for i in ur:
            newBoard[i] = turn
    if dr != False:
        for i in dr:
            newBoard[i] = turn
    if dl != False:
        for i in dl:
            newBoard[i] = turn
    return newBoard


def turnLeft(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 1
    j = [position]
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == 0:
            return False
        j.append(position - i)
        i += 1
        if board[position - i] == turn and board[position - i + 1] == oposite:
            return j


def turnRight(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 1
    j = [position]
    while posible:
        if position + i > 63:
            return False
        if board[position + i] == '@':
            return False
        if board[position + i] == 0:
            return False
        j.append(position + i)
        i += 1
        if position + i > 63:
            return False
        if board[position + i] == turn and board[position + i - 1] == oposite:
            return j


def turnUp(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 8
    j = [position]
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == 0:
            return False
        j.append(position - i)
        i += 8
        if position - i < 0:
            return False
        if board[position - i] == turn and board[position - i + 8] == oposite:
            return j


def turnDown(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 8
    j = [position]
    while posible:
        if position + i > 63:
            return False
        if board[position + i] == '@':
            return False
        if board[position + i] == 0:
            return False
        j.append(position + i)
        i += 8
        if position + i > 63:
            return False
        if board[position + i] == turn and board[position + i - 8] == oposite:
            return j

# upper left diagonal


def turnD1(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 9
    j = [position]
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == 0:
            return False
        j.append(position - i)
        i += 9
        if position - i < 0:
            return False
        if board[position - i] == turn and board[position - i + 9] == oposite:
            return j

# upper right diagonal


def turnD2(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 7
    j = [position]
    while posible:
        if position - i < 0:
            return False
        if board[position - i] == '@':
            return False
        if board[position - i] == 0:
            return False
        j.append(position - i)
        i += 7
        if position - i < 0:
            return False
        if board[position - i] == turn and board[position - i + 7] == oposite:
            return j

# lower right diagonal


def turnD3(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 9
    j = [position]
    while posible:
        if position + i > 63:
            return False
        if board[position + i] == '@':
            return False
        if board[position + i] == 0:
            return False

        j.append(position + i)
        i += 9
        if position + i > 63:
            return False
        if board[position + i] == turn and board[position + i - 9] == oposite:
            return j
# lower left diagonal


def turnD4(board, turn, position):
    oposite = mm.getOposition(turn)
    posible = True
    i = 7
    j = [position]
    while posible:
        if position + i > 63:
            return False
        if board[position + i] == '@':
            return False
        if board[position + i] == 0:
            return False
        j.append(position + i)
        i += 7
        if position + i > 63:
            return False
        if board[position + i] == turn and board[position + i - 7] == oposite:
            return j


#a = flipAll(b1, 1, 41)
#mm.analize(b1, 1, False, True)
