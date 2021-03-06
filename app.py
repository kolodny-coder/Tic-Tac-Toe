from utils import *


# WHILE LOOP TO KEEP RUNNING THE GAME
def app():
    print('Welcome to Tic Tac Toe')

    while True:
        # PLAY THE GAME

        game_mode = game_participants()
        marks_dict = choose_marks()
        player1_mark = marks_dict['player1_mark']
        player2_mark = marks_dict['player2_mark']

        # SET EVERYTHING UP (BOARD)
        the_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # GAME PLAY
        turn = 'unknown yet'
        game_on = True
        if game_mode == 1:
            turn = 'bot'
        if game_mode == 2:
            turn = 'player1'
        if game_mode == 3:
            turn = 'bot'
        player_mark = player2_mark
        bot_mark = player1_mark
        count = 0
        while game_on:

            if turn == 'bot':

                bot_turn(the_board, player1_mark, player2_mark)

                # Check if they won
                if check_for_win(the_board, player1_mark):
                    print('\n' * 5)
                    display_board(the_board)
                    print(f'The {player1_mark}\'s player has won!!\n\n')
                    break

                # Check if there is a tie
                elif full_board_check(the_board):
                    print("TIE game !!!\n\n")
                    game_on = False
                else:
                    if game_mode == 1:
                        turn = 'player2'
                    elif game_mode == 3:
                        turn = 'bot'
                        temp = player1_mark
                        player1_mark = player2_mark
                        player2_mark = temp


            # Player turn
            else:
                if turn == 'player2' or turn == 'player1':
                    # Chose a position
                    display_board(the_board)
                    position = player_choice(the_board)
                    place_marker(the_board, player_mark, position)
                    if check_for_win(the_board, player_mark):
                        display_board(the_board)
                        print(f'The {player_mark}\'s player has won!!')
                        break

                    if full_board_check(the_board):
                        display_board(the_board)
                        print("TIE game !!!")
                        break
                    else:
                        game_on = True

                        if game_mode == 1:
                            turn = 'bot'

                            player_mark = player2_mark
                        elif game_mode == 2:
                            turn = 'player1'
                            count += 1
                            players_marks_list = [player2_mark, player1_mark]
                            player_mark = players_marks_list[count % 2]

        if not reply():
            break


if __name__ == '__main__':
    app()
