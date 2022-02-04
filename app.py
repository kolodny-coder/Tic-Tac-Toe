def display_board(board):
    print('\n' * 1)

    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


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
        if space_check(board, i):
            return False

    return True


def check_for_draw(board):
    if (not (check_for_win(board, 'X')) and not (check_for_win(board, 'O')) and full_board_check(board)):
        return True
    else:
        return False


def player_choise(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose a free position (1-9) '))
    return position


def reply():
    choise = input('Do YOU want to play again? Y or N ').upper()
    return choise == 'Y'


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
                if score > best_score:
                    best_score = score

        return best_score

    else:
        best_score = 1000

        for indx, key in enumerate(board):
            if key == ' ':
                board[indx] = 'O'
                score = minmax(board, 0, True)
                board[indx] = ' '
                if score < best_score:
                    best_score = score

        return best_score


# WHILE LOOP TO KEEP RUNNING THE GAME
def app():
    print('Welocome to Tic Tac Toe')
    while True:
        # PLAY THE GAME

        # SET EVERYTHING UP (BOARD, WHOS FIRST)
        the_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # GAME PLAY
        play_game = input('Ready to play ? y or n  ')

        if play_game == 'y':
            game_on = True
        else:
            game_on = False
        turn = 'computer'
        while game_on:

            if turn == 'computer':
                # show the board
                display_board(the_board)

                # Chose a position

                comp_move(the_board)
                display_board(the_board)
                # Check if they won
                if check_for_win(the_board, 'X'):
                    display_board(the_board)
                    print('The computer has won!!')
                    break

                    # Check if there is a tie

                elif full_board_check(the_board):
                    # display_board(the_board)
                    print("TIE game !!!")
                    game_on = False
                else:
                    turn = 'player'

            # Player turn
            else:
                # Chose a position
                position = player_choise(the_board)
                place_marker(the_board, 'O', position)
                # display_board(the_board)
                if check_for_win(the_board, 'O'):
                    display_board(the_board)
                    print('The player has won!!')
                    break

                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE game !!!")
                    break
                else:
                    game_on = True

                    turn = 'computer'

        if not reply():
            break


if __name__ == '__main__':
    app()
