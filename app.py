from utils import *
import time

# WHILE LOOP TO KEEP RUNNING THE GAME
def app():
    print('Welocome to Tic Tac Toe')

    while True:
        # PLAY THE GAME
        while True:
            game_participates()
            # if game_participates == 1:
            #     print('human vs bot\n')
            #     player1_choice = int(input('choose your mark (1-2):\n 1. X\n 2. O\n\n'))
            #     if player1_choice == 1:
            #         players1_mark = 'X'
            #         bot_mark = 'O'
            #         break
            #     elif player1_choice == 2:
            #         players1_mark = 'X'
            #         bot_mark = 'O'
            #         break
            #     else:
            #         print('you chose invalid option please try agian :)\n')




            print('human vs bot')


    # SET EVERYTHING UP (BOARD)
        the_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # GAME PLAY

        game_on = True
        turn = 'computer'
        while game_on:

            if turn == 'computer':
                # show the board
                display_board(the_board)

                # Chose a position
                time.sleep(2)
                comp_move(the_board)
                display_board(the_board)
                # Check if they won
                if check_for_win(the_board, 'X'):
                    display_board(the_board)
                    print('The computer has won!!\n\n')
                    break

                # Check if there is a tie
                elif full_board_check(the_board):
                    print("TIE game !!!\n\n")
                    game_on = False
                else:
                    turn = 'player'

            # Player turn
            else:
                # Chose a position
                position = player_choice(the_board)
                place_marker(the_board, 'O', position)
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
