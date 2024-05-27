# SUDOKU SOLVER
def valid_number(board: list[list[str]], row: int, col: int, num: str) -> bool:
    # check the row
    if num in board[row]:
        return False
    # check the column
    if num in [board[i][col] for i in range(len(board))]:
        return False
    # check the 3x3 box
    if col < 3:
        start_col = 0
    elif col < 6:
        start_col = 3
    else:
        start_col = 6
    if row < 3:
        start_row = 0
    elif row < 6:
        start_row = 3
    else:
        start_row = 6
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    

def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    numbers: list[int] = [str(i) for i in range(1, 10)]
    if all('.' not in row for row in board):
        return True
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '.':
                for i in numbers:
                    if i not in board[row]:
                        if all(i != board[row1][col] for row1 in range(len(board))):
                            board[row][col] = i
                            valid_sudoku(board)
                            board[row][col] = '.'
    return False

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))