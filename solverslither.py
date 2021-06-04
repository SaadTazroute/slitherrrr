def solveSudokuHelper(i, j, board):
    if i == len( indexes[0]) and j == len(indexes):

        for x in range(1, 10):
            if isValid(i, j, x, board) is True:
                board[i][j] = x
                for row in board:
                    for ele in row:
                        print(ele, end=" ")
                    print()
                board[i][j] = 0


    if j > 8:
        solveSudokuHelper(i + 1, 0, board)
        return

    if board[i][j] == 0:
        for x in range(1, 10):
            if isValid(i, j, x, board) is True:
                board[i][j] = x
                solveSudokuHelper(i, j + 1, board)
                board[i][j] = 0
    else:
        solveSudokuHelper(i, j + 1, board)


    if statut (indexes,etat,case) :
        i = case[0]
        j= case[1]
        solver(i,j+1,etat,case)

    return