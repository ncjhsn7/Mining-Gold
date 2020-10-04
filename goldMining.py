# -------------------------------------------------------

txt = open("casoPDF.txt", "r")
boardLength = txt.readline()
board = [[0 for i in range(int(boardLength))] for j in range(int(boardLength))]
i = 0

for x in txt:
    x = x.split()
    j = 0
    for y in x:
        board[i][j] = int(y)
        j += 1
    i += 1

boardLength = int(boardLength)


def mining1(x, y):
    if x == 0 and y == boardLength - 1:
        return board[x][y]

    elif x == 0:
        return mining1(x, y+1) + board[x][y]

    elif y == boardLength-1:
        return mining1(x-1, y) + board[x][y]

    return max(mining1(x, y+1), mining1(x-1, y), mining1(x-1, y+1)) + board[x][y]

# ------------------------------------------------


savePath = {}
directions = []


def mining2(x, y):
    if x == 0 and y == boardLength - 1:
        return (board[x][y], " ")

    elif x == 0:
        if (x, y) not in savePath:
            goldValue = mining2(x, y+1)[0] + board[x][y]
            savePath[(x, y)] = (goldValue, "E")

    elif y == boardLength-1:
        if (x, y) not in savePath:
            goldValue = mining2(x-1, y)[0] + board[x][y]
            savePath[(x, y)] = (goldValue, "N")

    else:
        if (x, y) not in savePath:
            n = mining2(x-1, y)[0]
            e = mining2(x, y+1)[0]
            ne = mining2(x-1, y+1)[0]
            if n > e:
                if n > ne:
                    goldValue = n + board[x][y]
                    savePath[(x, y)] = (goldValue, "N")
                else:
                    goldValue = ne + board[x][y]
                    savePath[(x, y)] = (goldValue, "NE")

            elif e > n:
                goldValue = e + board[x][y]
                savePath[(x, y)] = (goldValue, "E")
            else:
                goldValue = ne + board[x][y]
                savePath[(x, y)] = (goldValue, "NE")
    return savePath[(x, y)]


def returnPath(x, y):
    if x == 0 and y == boardLength - 1:
        print(directions)
    else:
        directions.append(savePath[(x, y)][1])
        if savePath[(x, y)][1] == "N":
            returnPath(x-1, y)

        if savePath[(x, y)][1] == "E":
            returnPath(x, y+1)

        if savePath[(x, y)][1] == "NE":
            returnPath(x-1, y+1)

# -----------------------------------------

board2 = [[0 for i in range(int(boardLength))] for j in range(int(boardLength))]
def mining3():
    lastMove = board[0][boardLength-1]
    board2[0][boardLength-1] = (lastMove, " ")

    for x in range(0, boardLength, 1):
        for y in range(boardLength-1, -1, -1):
            if x != 0 or y != boardLength-1:
                if x == 0:
                    a = board[x][y] + board2[x][y+1][0]
                    board2[x][y] = (a, "E")
                elif y == boardLength-1:
                    b = board[x][y] + board2[x-1][y][0]
                    board2[x][y] = (b, "N")
                else:
                    n = board2[x-1][y][0]
                    e = board2[x][y+1][0]
                    ne = board2[x-1][y+1][0]
                    if n > e:
                        if n > ne:
                            goldValue = n + board[x][y]
                            board2[x][y] = (goldValue, "N")
                        else:
                            goldValue = ne + board[x][y]
                            board2[x][y] = (goldValue, "NE")
                    elif e > n:
                        goldValue = e + board[x][y]
                        board2[x][y] = (goldValue, "E")
                    else:
                        goldValue = ne + board[x][y]
                        board2[x][y] = (goldValue, "NE")
    returnPath2(boardLength-1, 0)
    return goldValue


directions2 = []
def returnPath2(x, y):
    for i in range(1,boardLength-1,1):
        for j in range(1,0,1):
            print(board2[i][j])

    if x == 0 and y == boardLength - 1:
        print(directions2)
    else:
        d = board2[x][y][1]
        directions2.append(d)
        if d == "N":
            returnPath2(x-1, y)

        if d == "E":
            returnPath2(x, y+1)

        if d == "NE":
            returnPath2(x-1, y+1)

# -----------------------------------------
print(mining1(boardLength-1, 0))
print()
print(mining2(boardLength-1, 0)[0])
print(returnPath(boardLength-1, 0))
print()
print(mining3())
