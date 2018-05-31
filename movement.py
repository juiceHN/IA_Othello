

b1 = [0, 2, 1, 1, 0, 0, 0, 0,
      0, 0, 1, 1, 2, 9, 8, 0,
      0, 0, 1, 1, 2, 1, 1, 1,
      0, 2, 2, 2, 2, 2, 1, 1,
      0, 0, 2, 1, 2, 2, 0, 1,
      0, 0, 0, 2, 2, 0, 2, 0,
      0, 0, 0, 2, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]

b2 = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 2, 1, 0, 0, 0,
      0, 0, 0, 1, 2, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]
# printBoard10(b1)

# printBoard10
# prints score and a mini board


def printBoard10(board_array):
    wp = 0
    bp = 0
    a = '  1 2 3 4 5 6 7 8  \n'
    for i in range(len(board_array)):
        if (i % 10) == 0 and i != 0:
            a = a + '\n'
        if board_array[i] == 0:
            a = a + '■ '
        elif board_array[i] == 2:
            a = a + '2 '
            wp = wp + 1
        elif board_array[i] == '@':
            a = a + '@ '
        elif board_array[i] == 1:
            a = a + '1 '
            bp = bp + 1
        else:
            a = a + '♫ '

    print(a)
    print('1: ', bp, '\n2: ', wp)

# printScore
# prints scores only


def printScore(board_array):
    wp = 0
    bp = 0
    for i in range(len(board_array)):
        if board_array[i] == 2:
            wp = wp + 1
        elif board_array[i] == 1:
            bp = bp + 1
    print('##########')
    print('# 1: ', bp)
    print('# 2: ', wp)

# parseBoard
# changes 8*8 arrray to 10*10
# for better analisis
# returns new 10*10 board arrray


def parseBoard(board):
    myBoard = []
    for i in range(10):
        myBoard.append('@')
    for i in range(len(board)):
        if i % 8 == 0:
            myBoard.append('@')
            myBoard.append(board[i])
        elif i % 8 == 7:
            myBoard.append(board[i])
            myBoard.append('@')
        else:
            myBoard.append(board[i])
    for i in range(10):
        myBoard.append('@')
    return myBoard


# checkBoard
# checks for posible movements
# returns an array full of all posible movements
# and returns a new board array (use to print and check)

def checkBoard(turn, board):
    moveArray = []
    final = []
    for i in range(len(board)):
        if board[i] == turn:
            l = checkLeft(i, board, turn)
            r = checkRight(i, board, turn)
            u = checkUp(i, board, turn)
            d = checkDown(i, board, turn)
            ul = checkD1(i, board, turn)
            ur = checkD2(i, board, turn)
            dr = checkD3(i, board, turn)
            dl = checkD4(i, board, turn)
            if l != False:
                moveArray.append(l)
            if r != False:
                moveArray.append(r)
            if u != False:
                moveArray.append(u)
            if d != False:
                moveArray.append(d)
            if ul != False:
                moveArray.append(ul)
            if ur != False:
                moveArray.append(ur)
            if dr != False:
                moveArray.append(dr)
            if dl != False:
                moveArray.append(dl)
    moveArray.sort()
    for i in moveArray:
        if i not in final:
            final.append(i)
    for i in moveArray:
        board[i] = '♫'
    return board, final


# checking all directions
# all check and Ds returns false if no available options
# or the last position for a possible movement

def checkLeft(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 1
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == turn:
            return False
        if board[position - i] == 0:
            if board[position - i + 1] == oposite:
                return position - i
            else:
                return False
        i += 1


def checkRight(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 1
    while posible:
        if board[position + i] == '@':
            return False
        if board[position + i] == turn:
            return False
        if board[position + i] == 0:
            if board[position + i - 1] == oposite:
                return position + i
            else:
                return False
        i += 1


def checkUp(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 10
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == turn:
            return False
        if board[position - i] == 0:
            if board[position - i + 10] == oposite:
                return position - i
            else:
                return False
        i += 10


def checkDown(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 10
    while posible:
        if board[position + i] == '@':
            return False
        if board[position + i] == turn:
            return False
        if board[position + i] == 0:
            if board[position + i - 10] == oposite:
                return position + i
            else:
                return False
        i += 10

# upper left diagonal


def checkD1(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 11
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == turn:
            return False
        if board[position - i] == 0:
            if board[position - i + 11] == oposite:
                return position - i
            else:
                return False
        i += 11


# upper right diagonal
def checkD2(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 9
    while posible:
        if board[position - i] == '@':
            return False
        if board[position - i] == turn:
            return False
        if board[position - i] == 0:
            if board[position - i + 9] == oposite:
                return position - i
            else:
                return False
        i += 9

# lower right diagonal


def checkD3(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 11
    while posible:
        if board[position + i] == '@':
            return False
        if board[position + i] == turn:
            return False
        if board[position + i] == 0:
            if board[position + i - 11] == oposite:
                return position + i
            else:
                return False
        i += 11

# lower left diagonal


def checkD4(position, board, turn):
    oposite = getOposition(turn)
    posible = True
    i = 9
    while posible:
        if board[position + i] == '@':
            return False
        if board[position + i] == turn:
            return False
        if board[position + i] == 0:
            if board[position + i - 9] == oposite:
                return position + i
            else:
                return False
        i += 9

# getOposition
# given a color or number
# returns opposite


def getOposition(turn):
    if turn == 1:
        return 2
    else:
        return 1

# parsnt
# converting 10*10 array possible values back to 8*8


def parsnt(values):
    new = []
    for i in values:
        if i > 10 and i <= 18:
            a = i - 11
        elif i > 18 and i <= 28:
            a = i - 13
        elif i > 28 and i <= 38:
            a = i - 15
        elif i > 38 and i <= 48:
            a = i - 17
        elif i > 48 and i <= 58:
            a = i - 19
        elif i > 58 and i <= 68:
            a = i - 21
        elif i > 68 and i <= 78:
            a = i - 23
        elif i > 78 and i <= 88:
            a = i - 25
        new.append(a)
    return new


def parseMove(i):
    if i < 8:
        i += 11
    elif i >= 8 and i < 16:
        i += 13
    elif i >= 16 and i < 24:
        i += 15
    elif i >= 24 and i < 32:
        i += 17
    elif i >= 32 and i < 40:
        i += 19
    elif i >= 40 and i < 48:
        i += 21
    elif i >= 48 and i < 56:
        i += 23
    elif i >= 56 and i < 64:
        i += 25
    return i
# analyze
# used to tie up everything
# receives 8*8 board array, turn number
# optional: score - for printing scores
# returns array of possible movements


def analize(board, turn, score=False, pb=False):
    a = parseBoard(board)
    b, posible = checkBoard(turn, a)
    if score == True:
        printScore(b)
    if pb == True:
        printBoard10(a)
    c = parsnt(posible)
    return c

def printBoard(board):
    a = parseBoard(board)
    printBoard10(a)
# analize(b2, 1, True, True)
