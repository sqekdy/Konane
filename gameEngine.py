from Player import Player
from Board import Board
import game as UI
import aiEngine
import copy
import math


class gameEngine():
    """This class is the main engine of this Konane Project which monitors the gameplay"""
    # AI is maximizing player

    available_moves = []  # For a particular game, we only maintain one global list that captures possibles moves


    # in a game state

    def __init__(self):

        print("\n\n\nWELCOME TO KONANE !!! Please bear with us, and provide the correct input for following questions ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        to_remove_f_row, to_remove_f_col = input("Please enter the row,column of 1st player to remove, eg., 56:  \n")
        to_remove_s_row, to_remove_s_col = input("Please enter the row,column of 2nd player to remove, eg., 57: \n ")

        self.game_players = []

        self.current_board=None

        opponent_type = input("Please choose your player type eg. black / white: ")
        self.ai_type = "black" if (opponent_type == "white") else "white"
        print("\n ------------------------------------------------------------------------------------------------")
        print("\n GREAT! Your player type is: {} . The AI is : {} ".format(opponent_type, self.ai_type))

        print("\n ====================BLACK STARTS FIRST============== RENDERING VISUAL...... ================")

        player_index = 99

        # This creates a total of 62 players, excluding two players from the user input, out of 64 players

        for i in range(8):
            for j in range(8):

                player_index += 1

                if (not ((i == int(to_remove_f_row) and j == int(to_remove_f_col))
                         or (i == int(to_remove_s_row) and j == int(to_remove_s_col)))):
                    identify_player_type = "black" if ((i + j) % 2 == 0) else "white"
                    new_player = Player(i, j, identify_player_type[0] + str(player_index), identify_player_type)
                    self.game_players.append(new_player)

        # DONE Initialize the board and proceed, continue friday morning

        # the following statement draws the board. commenting out as not needed now
        UI.draw_board(
            [(_each_player.cur_col_pos, _each_player.cur_row_pos) for _each_player in self.game_players])

        print([_.player_id for _ in self.game_players])

        pass





    def start_game(self):
        """ This method is where the game starts, initial state of the board is drawn, and two pieces of players are
        removed, provided by the user

        :return:
        """
        board_index = 99
        initial_depth = 0

        can_game_continue = True
        game_turn = 0 if self.ai_type == "black" else 1

        # creates an initial board with 62 players in it.
        self.current_board = Board("board" + str(board_index), self.game_players, self.ai_type, initial_depth, [])

        print("_____________")
        print(self.current_board.sef_value)

        while can_game_continue:  # Keeps the game going , until loss or draw on either sides

            gameEngine.available_moves = self.current_board.possible_play

            # After each move, check for a draw
            # TODO Update game cannot draw in konane ...hehehe

            # if len(gameEngine.available_moves) == 0:  # If no available move for current board, game is draw
            #
            #     print("Game over. Result is draw.")
            #
            #     break

            if (game_turn == 0):

                #TODO iterate through players and fetch the players in possible moves in board, and distinguish
                # between black and white possible moves

                # We do not want to change the state of the main game board, while minimax performs forward searching.
                # A good approach would be to create a duplicate board object of current board and pass that to the function.
                # This way we can maintain main game board, and experimental search board for the AI.
                #AI is maximizing player

                is_updated = False
                ai_move_p_row = ai_move_p_col = ai_move_d_row = ai_move_d_col = None
                search_board = copy.deepcopy(self.current_board)

                best_move_sef, play = aiEngine.minimax(search_board, 3, float("-inf"), float("inf"), True)

                for k,v in play.items():

                        ai_move_p_row, ai_move_p_col, ai_move_d_row, ai_move_d_col = v
                        is_updated = self.current_board.update_board(ai_move_d_row,
                                                                     ai_move_d_col,
                                                                     ai_move_p_row,
                                                                     ai_move_p_col)

                        break

                if is_updated:
                    print ("AI move is: ", ai_move_p_row,ai_move_p_col, " to ", ai_move_d_row, ai_move_d_col)

                    UI.draw_board(
                        [(_each_player.cur_col_pos, _each_player.cur_row_pos) for _each_player in
                         self.current_board.player_list])


                game_turn = 1  # Opponent move here

            elif (game_turn == 1):

                # TODO   Make event handler for UI, to register and capture move
                #       For time being, input prompt works just fine, Implement UI if time permits
                #       Note that to give the next input, one need to close the pygame window, so that console frees up
                #       A good implementation might be to power up the board in separate thread so that we have control
                #       over the console window and the pygame window at the same time.

                while True:

                    try:
                        player_row, player_col = map(int,tuple(input(
                            "Please enter row, column of player to move for eg, 25, where 2 is row, and 5 is column: ")))


                        player_transfer_row, player_transfer_column = map(int,tuple(input(
                        "Please enter a valid move, for eg., 23, where 2 is row and 3 is column: ")))

                    except Exception:
                        print("Invalid input. Please try again")
                        continue

                    break


                self.current_board.update_board(player_transfer_row, player_transfer_column,
                                           player_row, player_col)

                UI.draw_board(
                    [(_each_player.cur_col_pos, _each_player.cur_row_pos) for _each_player in self.current_board.player_list])


                game_turn = 0  # Next move is AI move


if __name__ == "__main__":
    game = gameEngine()
    game.start_game()
