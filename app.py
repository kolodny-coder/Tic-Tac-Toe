from utils import *

# WHILE LOOP TO KEEP RUNNING THE GAME
def app():
    print('Welocome to Tic Tac Toe')
    while True:
        # PLAY THE GAME

        # SET EVERYTHING UP (BOARD)
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
