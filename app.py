def display_board(board):
    print('\n' * 100)

    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


# board = [' ']* 10
board = ['#', ' ', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X']


# display_board(board)

def place_marker(board, mark, position):
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
        print(i)
        if space_check(board, i):
            return False

    return True

def player_choise(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose a free postion (1-9) '))
    return position


display_board(board)
print(player_choise(board))
#
# display_board(board)
# print(full_board_check(board))
# print(check_for_win(board, 'X'))
