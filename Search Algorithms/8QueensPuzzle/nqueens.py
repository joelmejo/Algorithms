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

# quindi si può dedurre che una volta posizionata una donna, non si possono più posizionare altre donne
#   sulla stessa riga, colonna e diagonali

# quindi si potrebbe creare una lista che contiene tutte le posizioni gia escluse cosi da non ricontrollarle ogni volta
def n_queens_puzzle(n: int):
    # nxn chess board
    chess_board: list[list[int]] = [[0 for column in range(n)] for row in range(n)]
    rows_in_use: dict = {}
    columns_in_use: dict = {}
    for i in range(n):
        rows_in_use[i] = False
        columns_in_use[i] = False

    #############################################################
    # COLLECTIONS TO STORE ESSENTIAL DATA


    ########################
    # RESULTS

    # list to store the results
    results: list= []


    ########################
    # DATA STORED UNTIL A RESULT IS FOUND

    # dictionary to store the queens positioned
    queens_positioned: dict[tuple] = {}

    # dictionary to store the columns in use
    columns_in_use: dict = {}

    # dictionary to store the rows in use
    rows_in_use: dict = {}


    # dictionary to store the visited positions of the queens in use, and of the next queen that we have already visited
    visited_positions: dict[list[tuple]] = {0: []}
    
    #############################################################
    # FUNCTIONS

    # controllo diagonale
    def check_diagonal(row: int, column: int, chess_board_lenght: int) -> bool:
        column_right: int = column
        column_left: int = column
        row_down: int = row
        row_up: int = row

        for i in range(max((len(chess_board[row]) - 1) - row, row, (len(chess_board[row]) - 1) - column, column)):
            column_right += 1
            column_left -= 1
            row_down += 1
            row_up -= 1
            # diagonale destra basso
            if column_right <= chess_board_lenght and row_down <= chess_board_lenght:
                if chess_board[row_down][column_right] == 1:
                    return False
            # diagonale sinistra alto
            if column_left >= 0 and row_up >= 0:
                if chess_board[row_up][column_left] == 1:
                    return False
            # diagonale sinistra basso
            if column_left >= 0 and row_down <= chess_board_lenght:
                if chess_board[row_down][column_left] == 1:
                    return False
            # diagonale destra alto
            if column_right <= chess_board_lenght and row_up >= 0:
                if chess_board[row_up][column_right] == 1:
                    return False
        return True
    
    def recursive_dfs(chess_board: list[list[int]], queens_positioned: dict):
        row: int = queens_positioned[len(queens_positioned) - 1][0]
        column: int = queens_positioned[len(queens_positioned) - 1][1]


        
    for row in range(n):
        for column in range(n):
            if [row, column] in visited_positions[0]:
                continue

            # add the queen to the chess_board
            chess_board[row][column] = 1

            # add the queen just positioned on the chess_board to the queens_positioned dictionary
            queens_positioned[0] = (row, column)

            # append new first queen positioned on the chess_board to the visited_positions dictionary
            visited_positions[0].append((row, column))

            # change the status of the row and column in in_use dictionaryies
            rows_in_use[row] = True
            columns_in_use[column] = True
    
            
n_queens_puzzle(8)