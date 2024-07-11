# Il rompicapo (o problema) delle otto regine è un problema che consiste nel trovare il modo di posizionare otto donne (pezzo degli scacchi) su una scacchiera 8×8 tali che nessuna di esse possa catturarne un'altra,
# usando i movimenti standard della regina. Perciò, una soluzione dovrà prevedere che nessuna regina abbia una colonna, traversa o diagonale in comune con un'altra regina.
# Il problema delle otto regine è un esempio del più generale problema delle n regine, che consiste nel piazzare, con le condizioni illustrate precedentemente, n regine su una scacchiera n × n; in questa forma,
# in particolare, esso viene spesso usato per illustrare tecniche di progettazione di algoritmi e di programmazione. È stato dimostrato matematicamente che il problema è risolvibile per n = 1 o n ≥ 4, mentre non lo è per n = 2 e n = 3.

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


#############################################################
# FUNCTIONS

# knowing that the queen is positioned row by row it only checks the upper part from the possible position of the queen
def is_safe(row: int, col: int, chess_board: list[list[int]], chess_board_lenght: int) -> bool:
    # check the upper part of the column
    for i in range(row):
        if chess_board[i][col] == 1:
            return False
    
    # check the upper part of the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chess_board[i][j] == 1:
            return False
    
    # check the upper part of the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, chess_board_lenght)):
        if chess_board[i][j] == 1:
            return False

    return True

# recursive function to place the queens
def solve_n_queens(board, row, solutions):
    # base case: if all queens are placed, add the solution to the list
    if row >= len(board):
        solutions.append([row[:] for row in board])
        return
    
    # try to place a queen in each column of this row
    for i in range(len(board)):
        if is_safe(row, i, board, len(board)):
            # place the queen
            board[row][i] = 1

            # recursively place the other queens
            solve_n_queens(board, row + 1, solutions)

            # if placing the queen does not lead to a solution, remove it (backtrack)
            board[row][i] = 0

# function to print the board
def print_board(board):
    for row in board:
        print(row)

# function to solve the n queens problem
def solve(n: int = 8):
    # n x n chess board
    # board = [[0] * n for _ in range(n)]
    board: list[list[int]] = [[0 for column in range(n)] for row in range(n)]
    solutions = []

    solve_n_queens(board, 0, solutions)
    
    print(f"Trovate {len(solutions)} soluzioni.")
    for sol in solutions:
        print_board(sol)
        print()
    print(f"Trovate {len(solutions)} soluzioni.")

solve()
            
        

# SOLUZIONE GPT
def is_safe(board, row, col):
    # Controlla la riga a sinistra
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Controlla la diagonale in alto a sinistra
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Controlla la diagonale in basso a sinistra
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board: int, col: int, solutions: list):
    # Caso base: se tutte le regine sono piazzate, aggiungi la soluzione alla lista
    if col >= len(board):
        solutions.append([row[:] for row in board])
        return

    # Prova a piazzare una regina in ogni riga di questa colonna
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Piazza la regina
            board[i][col] = 1

            # Ricorsivamente piazza le altre regine
            solve_n_queens(board, col + 1, solutions)

            # Se piazzare la regina non porta a una soluzione, rimuovila (backtrack)
            board[i][col] = 0

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def solve():
    n = 8
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, solutions)
    
    print(f"Trovate {len(solutions)} soluzioni.")
    for sol in solutions:
        print_board(sol)

solve()
