board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]
game_still_going = True

winner = None
current_player = 'x'





def play_game():

    dis_board()

    while game_still_going:

        handle_turn(current_player)
        check_if_gameover()
        flip_player()

    if winner == 'x' or winner == 'o':
        print(f'{winner} won')
    elif winner == None:
        print('Tied')

def dis_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def handle_turn(player):

    position = input('Enter the position in between 1-9:  ')
    position = int(position) - 1
    board[position] = player
    dis_board()


def check_if_gameover():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return




def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[2] != "_"
    column_2 = board[1] == board[4] == board[5] != "_"
    column_3 = board[6] == board[7] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None




def check_diagonals():

    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    else:
        return None


def check_if_tie():
    global game_still_going

    if '-' not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player

    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'
    return

play_game()


