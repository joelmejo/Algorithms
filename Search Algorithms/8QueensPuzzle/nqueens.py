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

########################
# RESULTS

# list to store the results
results: list= []


#############################################################
# FUNCTIONS

# function to check if the diagonal is safe
# knowing that the queen is positioned row by row it only checks the upper part of the diagonal from the possible position of the queen
def check_diagonal(row: int, column: int, chess_board: list[list[int]], chess_board_lenght: int) -> bool:
    column_right: int = column
    column_left: int = column
    row_up: int = row

    for i in range(max(row, (len(chess_board[row]) - 1) - column, column)):
        column_right += 1
        column_left -= 1
        row_up -= 1
        # diagonale sinistra alto
        if column_left >= 0 and row_up >= 0:
            if chess_board[row_up][column_left] == 1:
                return False
        # diagonale destra alto
        if column_right <= chess_board_lenght and row_up >= 0:
            if chess_board[row_up][column_right] == 1:
                return False
    return True


# recursive function to position the queens on the chess_board
def recursive_dfs(chess_board: list[list[int]], chess_board_lenght: int, queens_positioned: dict[tuple[int]], columns_in_use: dict, visited_positions: dict[list[tuple]]):
    # knowing that the queen is positioned row by row, we can start from the row next to the last queen positioned
    for row in range((queens_positioned[len(queens_positioned) - 1[0]] + 1),chess_board_lenght):
        # DEPRECATED
        # # if the row is already in use, then skip it
        # if rows_in_use[row] == True:
        #     continue
        for column in range(chess_board_lenght):
            # if the column is already in use, then skip it
            if columns_in_use[column] == True:
                continue

            # if the position is already visited, then skip this position
            if [row, column] in visited_positions[len(queens_positioned)]: 
                continue
            # if the diagonal is not safe, then skip this position
            if not check_diagonal(row, column, chess_board, chess_board_lenght):
                continue
            else:
                # add the queen to the chess_board
                chess_board[row][column] = 1

                # add the queen just positioned on the chess_board to the queens_positioned dictionary
                queens_positioned[len(queens_positioned)] = (row, column)

                # if the number of queens positioned is equal to the chess_board_lenght, then we have a solution
                if len(queens_positioned) == chess_board_lenght:
                    return chess_board.copy()
                else:
                    # change the state of the new row and column in use in the rows_in_use and columns_in_use dictionaries
                    # rows_in_use[row] = True
                    columns_in_use[column] = True

                    # append new queen positioned on the chess_board to the visited_positions dictionary
                    visited_positions[len(queens_positioned)].append((row, column))

                    # recursive call to the function
                    recursive_dfs(chess_board, chess_board_lenght)

    # if we have not found a position safe for the new queen, then we have to backtrack
    
    # remove the last queen positioned from the chess_board
    chess_board[queens_positioned[len(queens_positioned) - 1][0]][queens_positioned[len(queens_positioned) - 1][1]] = 0

    # change the state of the row and column in use in the rows_in_use and columns_in_use dictionaries
     # rows_in_use[queens_positioned[len(queens_positioned) - 1][0]] = False
    columns_in_use[queens_positioned[len(queens_positioned) - 1][1]] = False

    # remove the last queen positioned from the queens_positioned dictionary
    queens_positioned.pop(len(queens_positioned) - 1)

    # if the newt queen was previusly positioned, then remove it from the visited_positions dictionary
    if (len(queens_positioned) + 1) in visited_positions:
        visited_positions.pop(len(queens_positioned) + 1)
    
                # 0 1 2 3 4 5 6 7 8 len 9
            # tried 0 1 2 3 4 5 6 7 8 len 10
                # rimuovo l'ultima posizione provata
                # 0 1 2 3 4 5 6 7 len 8
            # tried 0 1 2 3 4 5 6 7 8 len 10
                # rimuovo l'ultima posizione provata
                # 0 1 2 3 4 5 6 len 7
                # quindi len 7 + 1 = 8
                # elimino la 8ava regina da tried
                # tried 0 1 2 3 4 5 6 7 len 8
    if len(queens_positioned) > 0:
        # recursive call to the function
        recursive_dfs(chess_board, chess_board_lenght)
    else:
        return None

def n_queens_puzzle(n: int):
    
    #############################################################
    # COLLECTIONS TO STORE ESSENTIAL DATA UNTIL A RESULT IS FOUND

    # n x n chess board
    chess_board: list[list[int]] = [[0 for column in range(n)] for row in range(n)]
    # rows_in_use: dict = {}
    columns_in_use: dict = {}
    for i in range(n):
        # rows_in_use[i] = False
        columns_in_use[i] = False

    # dictionary to store the queens positioned
    queens_positioned: dict[tuple[int]] = {}

    # dictionary to store the visited positions of the queens in use, and of the next queen that we have already visited
    visited_positions: dict[list[tuple]] = {0: []}
    
    
    # cicle to position the first queen
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
            # rows_in_use[row] = True
            columns_in_use[column] = True

            # call to the recursive function
            result = recursive_dfs(chess_board, n, queens_positioned, columns_in_use, visited_positions)

            if result != None:
                results.append(result)
    
            
n_queens_puzzle(8)