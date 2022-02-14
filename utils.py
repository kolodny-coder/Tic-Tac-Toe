import time


def get_decorator(errors=(Exception,), default_value=''):
    def decorator(func):

        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print('\n\nPlease choose a valid value\n\n ')
                return new_func(*args, **kwargs)

        return new_func

    return decorator


input_validator = get_decorator((ValueError), default_value='invalid value')


def display_board(board):
    print('\n' * 1)
    print('            |   |' + '\t\t\t' + '             |   |')
    print('          ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '\t\t\t' + '           1 | 2 | 3')
    print('            |   |' + '\t\t\t' + '             |   |')
    print('        --------------' + '\t\t\t' + '        --------------')
    print('            |   |' + '\t\t\t' + '             |   |')

    print('          ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '\t\t\t' + '           4 | 5 | 6')
    print('            |   |' + '\t\t\t' + '             |   |')
    print('        --------------' + '\t\t\t' + '        --------------')
    print('            |   |' + '\t\t\t' + '             |   |')
    print('          ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\t\t\t' + '           7 | 8 | 9')
    print('            |   |' + '\t\t\t' + '             |   |')


def place_marker(board, mark, position):
    board[position] = mark
    board[position] = mark


def check_for_win(board, mark):
    # Check if all rows share the same marker
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark)
            )


def space_check(board, position):
    free_spots = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if board[position] in free_spots:
        return True


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def check_for_draw(board):
    if not (check_for_win(board, 'X')) and not (check_for_win(board, 'O')) and full_board_check(board):
        return True
    else:
        return False


@input_validator
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose a free position (1-9)\n\n '))

    return position


@input_validator
def reply():
    choice = int(input('Do YOU want to play again? 1 for yes 2 for no '))
    return choice == 1


def comp_move(board, player1_mark, player2_mark):
    best_score = -1000
    best_move = 0

    for indx, key in enumerate(board):
        if key == ' ':
            board[indx] = player1_mark
            score = minmax(board, 0, False, player1_mark, player2_mark)
            board[indx] = ' '
            if score > best_score:
                best_score = score
                best_move = indx
    place_marker(board, player1_mark, best_move)
    return


def minmax(board, depth, is_maximazing, player1_mark, player2_mark):
    if check_for_win(board, player1_mark):
        return 100
    elif check_for_win(board, player2_mark):
        return -100
    elif check_for_draw(board):
        return 0

    if is_maximazing:
        best_score = -1000

        for indx, key in enumerate(board):
            if key == ' ':
                board[indx] = player1_mark
                score = minmax(board, 0, False, player1_mark, player2_mark)
                board[indx] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 1000

        for indx, key in enumerate(board):
            if key == ' ':
                board[indx] = player2_mark
                score = minmax(board, 0, True, player1_mark, player2_mark)
                board[indx] = ' '
                best_score = min(score, best_score)

        return best_score


@input_validator
def game_participants():
    while True:

        game_participates = int(input('please choose (1-3)\n 1. player vs bot\n 2. human vs player\n 3. bot vs bot '))

        if game_participates == 1:
            print('human vs bot\n')
            return 1
        elif game_participates == 2:
            print('human vs human\n')
            return 2
        elif game_participates == 3:
            print('bot vs bot\n')
            return 3
        else:
            print('\n\nYou chose invalid option please choose a number between 1 - 3 try again \n\n')


@input_validator
def choose_marks():
    while True:
        chosen_mark = int(input('Please choose your mark (1-2)\n 1. O\n 2. X\n\n  '))

        if chosen_mark == 1:
            print('you\'ll Play the O\'s and your opponent will play the X\'s  ')
            return {'player1_mark': 'X',
                    'player2_mark': 'O'}
        elif chosen_mark == 2:
            print('you\'ll Play the X\'s  and your opponent will play the O\'s  ')
            return {'player1_mark': 'O',
                    'player2_mark': 'X'}
        else:
            print('You Picked invalid option please pick int between (1-2)')


def bot_turn(board, player1_mark, player2_mark):
    print('\n' * 5)
    display_board(board)
    time.sleep(0.5)
    comp_move(board, player1_mark, player2_mark)
    print('\n' * 5)
    display_board(board)
