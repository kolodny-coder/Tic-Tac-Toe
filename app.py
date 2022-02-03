from computer_strategy import comp_return_position


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


# def computer_choise(board):
#     if board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
#         return  1
#     elif board == [' ', 'X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']:
#         return 9
#     elif board == [' ', 'X', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'X']:
#         return 7
#     elif board != [' ', 'X', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'X']:
#         return 7

def player_choise(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose a free position (1-9) '))
    return position


def reply():
    choise = input('Do YOU want to play again? Yes or NO  ').upper()
    return choise == 'Y'


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welocome to Tic Tac Toe')
while True:
    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHOS FIRST)
    the_board = [' '] * 10
    # GAME PLAY
    # play_game = input('Ready to play ? y or n  ')

    # if play_game == 'y':
    if 'y' == 'y':
        game_on = True
    else:
        game_on = False
    turn = 'computer'
    while game_on:

        if turn == 'computer':
            # show the board
            display_board(the_board)
            # Chose a position
            position = comp_return_position(the_board)
            # place the marker at the

            place_marker(the_board, 'X', position)
            display_board(the_board)
            # Check if they won
            if check_for_win(the_board, 'X'):
                display_board(the_board)
                print('The computer has won!!')
                game_on = False
                # Check if there is a tie

                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE game !!!")
                    game_on = False
                else:

                    turn = 'player'

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE game !!!")
                    game_on = False
                else:
                    turn = 'player'
        # Player turn
        else:
            display_board(the_board)
            # Chose a position
            position = player_choise(the_board)
            place_marker(the_board, 'O', position)
            display_board(the_board)
            if check_for_win(the_board, 'O'):
                display_board(the_board)
                print('The player has won!!')
                game_on = False
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE game !!!")
                    game_on = False
                else:
                    game_on = True

                    turn = 'computer'
            turn = 'computer'

    if not reply():
        break

    # BRAK OUT OF THE WHILE LOOP ON reply()

#
# display_board(board)
# print(player_choise(board))
#
# display_board(board)
# print(full_board_check(board))
# print(check_for_win(board, 'X'))
