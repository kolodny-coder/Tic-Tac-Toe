from utils import *
import time

# WHILE LOOP TO KEEP RUNNING THE GAME
def app():
    print('Welocome to Tic Tac Toe')

    while True:
        # PLAY THE GAME

        game_mode = game_participants()
        marks_dict = choose_marks()
        player1_mark = marks_dict['player1_mark']
        player2_mark = marks_dict['player2_mark']



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
                time.sleep(0.5)
                comp_move(the_board, player1_mark, player2_mark)
                display_board(the_board)
                # Check if they won
                if check_for_win(the_board, player1_mark):
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
                place_marker(the_board, player2_mark, position)
                if check_for_win(the_board, player2_mark):
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
