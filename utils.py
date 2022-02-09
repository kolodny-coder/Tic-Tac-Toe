def display_board(board):
    print('\n' * 1)
    print('            |   |')
    print('          ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('            |   |')
    print('        --------------')
    print('            |   |')

    print('          ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('            |   |')
    print('        --------------')
    print('            |   |')
    print('          ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('            |   |')


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
    return board[position] == ' '


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


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose a free position (1-9)\n\n '))

    return position


def reply():
    choice = int(input('Do YOU want to play again? 1 for yes 2 for no '))
    return choice == 1


def comp_move(board):
    best_score = -1000
    best_move = 0

    for indx, key in enumerate(board):
        if key == ' ':
            board[indx] = 'X'
            score = minmax(board, 0, False)
            board[indx] = ' '
            if score > best_score:
                best_score = score
                best_move = indx
    place_marker(board, 'X', best_move)
    return


def minmax(board, depth, is_maximazing):
    if check_for_win(board, 'X'):
        return 100
    elif check_for_win(board, 'O'):
        return -100
    elif check_for_draw(board):
        return 0

    if is_maximazing:
        best_score = -1000

        for indx, key in enumerate(board):
            if key == ' ':
                board[indx] = 'X'
                score = minmax(board, 0, False)
                board[indx] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 1000

        for indx, key in enumerate(board):
            if key == ' ':
                board[indx] = 'O'
                score = minmax(board, 0, True)
                board[indx] = ' '
                best_score = min(score, best_score)

        return best_score


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
            print('You chose invalid option please try again \n\n')

# display_board(['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
# display_board(['#', 'x', 'x', 'o', 'o', 'o', 'o','o', 'x', 'x'])
