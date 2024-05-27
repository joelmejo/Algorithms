# Considerazioni
# la regina si muove in diagonale, verticale e orizzontale
# * ^ ^ ^ * ^ ^ ^ *
# ^ * ^ ^ * ^ ^ * ^
# ^ ^ * ^ * ^ * ^ ^
# ^ ^ ^ * * * ^ ^ ^
# * * * * Q * * * *
# ^ ^ ^ * * * ^ ^ ^
# ^ ^ * ^ * ^ * ^ ^
# ^ * ^ ^ * ^ ^ * ^
# * ^ ^ ^ * ^ ^ ^ *


# ^ * ^ ^ * ^ ^ *
# ^ ^ * ^ * ^ * ^
# ^ ^ ^ * * * ^ ^
# * * * * Q * * *
# ^ ^ ^ * * * ^ ^
# ^ ^ * ^ * ^ * ^
# ^ * ^ ^ * ^ ^ *
# * ^ ^ ^ * ^ ^ ^

def isSafe(row: int, col: int, board: list[list[int]]) -> True:
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    for i in range(min(row, col) + 1):
        if board[row - i][col - i] == 1:
            return False
    
    for i in range(min(row, len(board) - col - 1) + 1):
        if board[row - i][col + i] == 1:
            return False
    return True
    
def solve_queens_andrea(n: int) -> list:
    board: list[list] = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        board.append(row)
        
    # scorri righe
    row = 0
    while (row < n):
        # scorri colonne
        k = 0
        if 1 in board[row]:
            k = board[row].index(1) + 1
            board[row][board[row].index(1)] = 0
        for col in range(k, n):
            if isSafe(row, col, board):
                board[row][col] = 1
                row += 1
                break 
        else:
            row -= 1    
    return board

def printBoard(board: list[list]):
    for row in board:
        print(row)
printBoard(solve_queens_andrea(8))
            