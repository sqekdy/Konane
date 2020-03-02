from Player import Player
from Board import Board
import game as UI
# import aiEngine
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

    def fetch_player(self,r_p, c_p):
        """
        :param r_p:  Row position of the player to be returned
        :param c_p: Column position of player to be returned
        :return: Player object, that matches the r_p and c_p values, present in the game_players list object
        """
        #TODO Catch stop iteration and print that not a valid game player information

        # The player object is determined by fetching the first item of generator object.
        # Care must be taken, not to have identical objects with same row pos and same col pos in the board.

        returned_player = (_ for _ in self.game_players
                           if _.return_player(r_p, c_p) is not None)

        return next(returned_player)

    def is_game_over(self):
        """ This function checks whether a game is over or not, based on the values computed by sef.
            i.e., if either player has 0 moves for (1 or 2 or 3 possible hops), then game is over, and
            other player wins the game

        :return: boolean value that indicates whether game is over or not, True-> game over ; False-> not over
        """

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
        current_board = Board("board" + str(board_index), self.game_players, self.ai_type, initial_depth, [])

        print("_____________")
        print(current_board.sef_value)

        while can_game_continue:  # Keeps the game going , until loss or draw on either sides

            gameEngine.available_moves = current_board.possible_play

            # After each move, check for a draw

            if len(gameEngine.available_moves) == 0:  # If no available move for current board, game is draw

                print("Game over. Result is draw.")

                break

            if (game_turn == 0):

                # TODO Make a move here. AI plays here. Call minimax function from aiEngine

                game_turn = 1  # Opponent move here

            elif (game_turn == 1):

                # TODO   Make event handler for UI, to register and capture move
                #       For time being, input prompt works just fine, Implement UI if time permits

                player_row, player_col = map(int,tuple(input(
                    "Please enter row, column of player to move for eg, 25, where 2 is row, and 5 is column: ")))


                player_transfer_row, player_transfer_column = map(int,tuple(input(
                    "Please enter a valid move, for eg., 23, where 2 is row and 3 is column: ")))


                current_board.update_board(player_transfer_row, player_transfer_column,
                                           self.fetch_player(player_row, player_col), self.game_players)

                UI.draw_board(
                    [(_each_player.cur_col_pos, _each_player.cur_row_pos) for _each_player in self.game_players])


                #game_turn = 0  # Next move is AI move


if __name__ == "__main__":
    game = gameEngine()
    game.start_game()
