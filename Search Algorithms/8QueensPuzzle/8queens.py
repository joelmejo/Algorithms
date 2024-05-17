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

# quindi si può dedurre che una volta posizionata una donna, non si possono più posizionare altre donne
#   sulla stessa riga, colonna e diagonali

# quindi si potrebbe creare una lista che contiene tutte le posizioni gia escluse cosi da non ricontrollarle ogni volta
from time import sleep

chess_board = [[0 for column in range(8)] for row in range(8)]

results: list= []
queens_positioned: dict = {}
columns_in_use: dict = {}
rows_in_use: dict = {}
tried_positions: dict = {}
new_position_available: bool = False

def check_diagonal(row, column):
    column_right = column
    column_left = column
    row_down = row
    row_up = row
    # diagonale principale
    # for i in range(max(len(chess_board[row]) - row, abs(row - len(chess_board[row])), len(chess_board[row]) - column, abs(column - len(chess_board[row])))):
    for i in range(8):
        column_right += 1
        column_left -= 1
        row_down += 1
        row_up -= 1
            # diagonale destra basso
        if column_right <= 7 and row_down <= 7:
            if chess_board[row_down][column_right] == 1:
                return False
        # diagonale sinistra alto
        if column_left >= 0 and row_up >= 0:
            if chess_board[row_up][column_left] == 1:
                return False
        # diagonale sinistra basso
        if column_left >= 0 and row_down <= 7:
            if chess_board[row_down][column_left] == 1:
                return False
        # diagonale destra alto
        if column_right <= 7 and row_up >= 0:
            if chess_board[row_up][column_right] == 1:
                return False
    return True

def check_row(row) -> bool:
    if 1 in chess_board[row]:
        return False
    return True

def check_column(column) -> bool:
    for i in range(8):
        if chess_board[i][column] == 1:
            return False
        else:
            return True

def is_safe(row, column) -> bool:
    if check_row(row) and check_column(column) and check_diagonal(row, column):
        return True
    else:
        return False

def place_queen() -> bool:
    global new_position_available
    for row in range(8):
        if row in rows_in_use:
            continue
        for column in range(8):
                if column in columns_in_use:
                    continue
                if len(queens_positioned) in tried_positions:
                    if (row, column) in tried_positions[len(queens_positioned)]:
                        continue
                if is_safe(row, column):
                    chess_board[row][column] = 1
                    rows_in_use[row] = row
                    columns_in_use[column] = column
                    queens_positioned[len(queens_positioned)] = (row, column)
                    if len(queens_positioned) - 1 in tried_positions:
                        list = tried_positions[len(queens_positioned) - 1]
                        list.append((row, column))
                    else:
                        tried_positions[len(queens_positioned) - 1] = [(row, column)]
                    new_position_available = True
                    for row in chess_board:
                        print(row)
                    print(queens_positioned)
                    print(tried_positions)
                    #time.sleep(3)
                    return True
            # if len(queens_positioned) - 1 in tried_positions:
            #     list = tried_positions[len(queens_positioned) - 1]
            #     list.append((row, column))
            # else:
            #     tried_positions[len(queens_positioned) - 1] = [(row, column)]
            #     chess_board[row][column] = 0
    row, column = queens_positioned.pop(len(queens_positioned) - 1)
    rows_in_use.pop(row)
    columns_in_use.pop(column)
    chess_board[row][column] = 0
    if len(queens_positioned) + 1 in tried_positions:
        tried_positions.pop(len(queens_positioned))
    new_position_available = False
    return False
    
    
while len(queens_positioned) < 8:
    new_position_available = True
    while new_position_available == True:
        new_position_available = False
        if not place_queen():
            new_position_available = False
        # if place_queen() == False:
        #     row, column = queens_positioned.pop(len(queens_positioned) - 1)
        #     if len(queens_positioned) - 1 in tried_positions:
        #         list = tried_positions[len(queens_positioned) - 1]
        #         list.append((row, column))
        #     else:
        #         tried_positions[len(queens_positioned) - 1] = [(row, column)]
        #         chess_board[row][column] = 0
        #     rows_in_use.pop(row)
        #     columns_in_use.pop(column)
        # else:
        #     new_position_available = True

results.append(chess_board)
for row in chess_board:
    print(row)
print(queens_positioned)

# il mio codice è andato in un loop infinito, perchè?

# GitHub Copilot
# Il tuo codice potrebbe andare in un loop infinito se non riesce a trovare una posizione valida per una regina e non riesce a tornare indietro per riposizionare le regine precedenti.

# Nel tuo codice, se place_queen() non riesce a trovare una posizione valida per una nuova regina, rimuove l'ultima regina posizionata e prova a trovare una nuova posizione per quella regina. Tuttavia, se non riesce a trovare una nuova posizione per l'ultima regina posizionata, continuerà a rimuovere la stessa regina e a cercare una nuova posizione per essa all'infinito, causando un loop infinito.

# Per risolvere questo problema, potresti dover aggiungere una logica per tornare indietro più passi se non riesci a trovare una nuova posizione per l'ultima regina posizionata. Ad esempio, potresti dover rimuovere l'ultima regina posizionata e la regina prima di quella, e poi cercare nuove posizioni per entrambe.

# Inoltre, potrebbe essere utile aggiungere qualche output di debug al tuo codice per aiutarti a capire esattamente dove si blocca. Potresti stampare il valore di queens_positioned, rows_in_use, columns_in_use, e tried_positions dopo ogni tentativo di posizionare una regina per vedere come cambiano questi valori nel tempo.

# joelmejo
# ok, in teoria se place_queen() non trova una possibile soluzione dovrebbe sempre eliminare l'ultima regina nella lista e così tornare indietro di un passo ogni volta che trova un vicolo cieco, perchè invece questo non accade?
# Il problema potrebbe essere dovuto al fatto che, quando place_queen() non riesce a trovare una posizione valida per una nuova regina, rimuove l'ultima regina posizionata e prova a trovare una nuova posizione per quella regina. Tuttavia, se non riesce a trovare una nuova posizione per l'ultima regina posizionata, continuerà a rimuovere la stessa regina e a cercare una nuova posizione per essa all'infinito, causando un loop infinito.

# Questo potrebbe accadere perché il codice non tiene traccia delle posizioni che ha già provato per ogni regina. Quindi, quando rimuove una regina, potrebbe finire per provare le stesse posizioni che ha già provato in precedenza, causando un loop infinito.

# Per risolvere questo problema, potresti dover aggiungere una logica per tenere traccia delle posizioni che hai già provato per ogni regina. Ad esempio, potresti aggiungere un dizionario tried_positions che mappa ogni regina alle posizioni che hai già provato per quella regina. Poi, quando provi a trovare una nuova posizione per una regina, puoi controllare questo dizionario per evitare di provare le stesse posizioni che hai già provato in precedenza.

# joelmejo
# in realtà place_queen() prende l'indice da rimuovere da queens_positioned prendendo la lunghezza di queen_positioned quindi in teoria ogni volta che viene eliminata una regina la lunghezza diminuisce quindi dovrebbe essere in grado di tornare indietro più di un passo
