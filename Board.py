from Player import Player  # Import the players class which defines the players attributes and behavior


class Board:
    # instance variable board layout is a 2-dimensional matrix having range (00,77)
    # board_layout example : { (3,4): pb12, }. This means at position row=3 and column=4, there is a black player with id of 12
    # We declare board_layout as instance variable (i.e, one board/object), because only one board view can exist at a particular time (i.e, state)
    # b and w are naming conventions for black players and white players respectively.
    # Naming convention for board_id would be b(followed by ascending number)
    # Initially, all the players in the board are "None" (or equivalently, null). We'll initialize them in following section

    # The initialization code i.e., constructor of this class as defined in the __init__ method below, also evaluates
    # Static Evaluation Function which is given as ,
    #
    #         [  +1  for each available single hop (for computer)  ]
    #         [  +2  for each available double hop (for computer)  ]
    #  f(S)=  [  +3  for each available triple hop (for computer)  ]
    #         [  -1  for each available single hop (for human)     ]
    #         [  -2  for each available double hop (for human)     ]
    #         [  -3  for each available triple hop (for human)     ]

    def __init__(self, board_id, player_list, AI_side, depth, play_collection):
        """This method initializes a board object. Each board has 64 players
        Input: A list of Player objects. Initially 62, but as game continues, the player count would decrease.
               Board_id which uniquely identifies the board.
        Returns: A board object with positioned players that is instantiated by the caller."""

        self.board_id = board_id
        self.player_list = player_list

        self.board_layout = {(x, y): None for x in range(8) for y in range(8)}

        # ai_type is either black or white
        self.ai_type = AI_side

        self.depth = depth

        for individual_player in player_list:
            player_row = individual_player.cur_row_pos
            player_col = individual_player.cur_col_pos
            player_id = individual_player.player_id

            # Get the row and column position on the board, and place the individual players one after another

            self.board_layout[(player_row, player_col)] = player_id

        self.possible_play = play_collection  # This captures all the possible moves in the board.
        # Data str is list. Final data str, however is  [{(row,col): (new_row,new_col)}, ..]
        # Each of these possible_play items will be the child in the game tree.

        self.sef_value = self.calculate_sef()

    def calculate_sef(self):
        """ This method calculates and returns the value of SEF for a particular board instance
        input: None, calls the total_available_moves_for_players inside the function
        :return: An integer number that could be +ve or -ve based on description of SEF.
        """

        ai_score, human_score = 0, 0

        sef_packed_data = self.total_available_moves_for_players()

        for k, v in sef_packed_data.items():

            if (k == self.ai_type):
                for hop_value in v:
                    for k1, v1 in hop_value.items():
                        ai_score += (k1 * v1)

            else:
                for hop_value2 in v:
                    for k2, v2 in hop_value2.items():
                        human_score -= (k2 * v2)

        return ai_score + human_score

    def fetch_player(self, r_p, c_p):
        """
        :param r_p:  Row position of the player to be returned
        :param c_p: Column position of player to be returned
        :return: Player object, that matches the r_p and c_p values, present in the game_players list object
        """
        # TODO Catch stop iteration and print that not a valid game player information

        # The player object is determined by fetching the first item of generator object.
        # Care must be taken, not to have identical objects with same row pos and same col pos in the board.

        returned_player = (_ for _ in self.player_list
                           if _.return_player(r_p, c_p) is not None)
        try:
            return next(returned_player) if not None else None

        except Exception as StopIteration:
            pass


    def total_available_moves_for_players(self):
        """This function computes necessary data for the Static Evaluation Function which determines the game strategy
           We captures the available moves for black and white players, and draw a tree based on these values of SEF
        Input: Board Object (current)
        Returns: compressed data for the static evaluation function, that contains available
                 moves for black and white, according to the hop length """

        # data structure to store hop length -> {color:[{hop_length:count}], color2:[{hop_length:count}] }

        self.possible_play = []

        data_for_sef = {"black": [{b: 0 for b in range(1, 4)}], "white": [{w: 0 for w in range(1, 4)}]}

        for cells_row_in_board in range(0, 8):  # Loop iterates through (0,0 to 7,7)
            for cells_col_in_board in range(0, 8):

                for fighter in self.player_list:

                    # We need to take into account, all available moves for a player in either direction.

                    if (fighter.can_move((cells_row_in_board, cells_col_in_board)) and
                            self.is_empty_cell(fighter.cur_row_pos, fighter.cur_col_pos,
                                               cells_row_in_board, cells_col_in_board)):

                       # print(fighter.cur_row_pos, fighter.cur_col_pos)
                       # print("can move")
                       # print(cells_row_in_board, cells_col_in_board)

                        self.possible_play.append(
                            {(fighter.cur_row_pos, fighter.cur_col_pos): (cells_row_in_board, cells_col_in_board)})

                        hop_length_row = abs(fighter.cur_row_pos - cells_row_in_board) // 2
                        hop_length_col = abs(fighter.cur_col_pos - cells_col_in_board) // 2
                        print("--------------------")
                        # The method can_move and is_empty_cell cannot conclude which direction the player is moving
                        # Therefore max( diff(row), diff(col) ) is returned to hop_length by lambda function

                        hop_length = (lambda a, b: a if a > b else b)(hop_length_row, hop_length_col)

                        player_count_to_increase = fighter.player_type

                        for list_item in data_for_sef[player_count_to_increase]:
                            for k, v in list_item.items():
                                if k == hop_length:
                                    list_item[k] += 1

        print(data_for_sef)
        return data_for_sef

    def is_empty_cell(self, c_row, c_col, dest_row, dest_col):
        """This method determines whether a dest. cell and all the required intermediate cells to hop into dest. cells is empty.
        Input: Dest. Cell Number i.e., in terms of row and column and the current cell number
        Returns: boolean value, True or False"""

        # We cannot afford to implement a move that goes from 6 ->7->0. This is board_out_of_bound exception.

        can_hop = False

        is_reverse_move = (dest_row < c_row or dest_col < c_col)

        # TODO Problem with static evaluation function determining the value of state
        # Mainly due to the reverse gamplay of player, not able to be implemented.
        # Pay attention to the for range function and -ve indexing
        # Update ----DONE------------

        move_direction_row_start, move_direction_row_end = (c_row, dest_row) if c_row < dest_row else (dest_row, c_row)
        move_direction_col_start, move_direction_col_end = (c_col, dest_col) if c_col < dest_col else (dest_col, c_col)

        if is_reverse_move:

            if (dest_col == c_col):

                can_hop = all(self.board_layout[(intermediate - 2), c_col] is None and self.board_layout[
                    (intermediate - 1), c_col] is not None
                              for intermediate in range(c_row, dest_row, -2))

            elif (c_row == dest_row):
                can_hop = all(self.board_layout[(dest_row, intermediate - 2)] is None and self.board_layout[
                    dest_row, (intermediate - 1)] is not None
                              for intermediate in range(c_col, dest_col, -2))
        else:

            if (dest_col == c_col):

                can_hop = all(self.board_layout[(intermediate + 2), c_col] is None and self.board_layout[
                    (intermediate + 1), c_col] is not None
                              for intermediate in range(c_row, dest_row, 2))

            elif (c_row == dest_row):
                can_hop = all(self.board_layout[(dest_row, intermediate + 2)] is None and self.board_layout[
                    dest_row, intermediate + 1] is not None
                              for intermediate in range(c_col, dest_col, 2))

        return can_hop

    def update_board(self, nrow, ncol, recent_pos_row, recent_pos_col):
        """Updates the board into another state
        Input: new_row, new_column for a player to move
                Player object (i.e., a player) to be updated . Note, only 1 update at a time
                Player list --> A list of players currently in the game
        Returns: A list of captured players to remove from the board"""

        to_be_updated_player=self.fetch_player(recent_pos_row,recent_pos_col)

        if to_be_updated_player == None:
            return False

        # player_id = to_be_updated_player.player_id TODO Redundant player information, not needed here, remove later

        # Check whether player can move and the cell where it is moving is empty or not
        if to_be_updated_player.can_move((nrow, ncol)) and self.is_empty_cell(recent_pos_row, recent_pos_col, nrow, ncol):



            # Update the new position for that player
            to_be_updated_player.cur_row_pos = nrow
            to_be_updated_player.cur_col_pos = ncol

            # Change the state of the board

            self.board_layout[(nrow, ncol)] = to_be_updated_player.player_id

            # Clear the earlier state of player in the board i.e, update to None
            self.board_layout[(recent_pos_row, recent_pos_col)] = None

            # Also remove any opponent in the way

            # TODO Remove the player as well i.e, reset the row and column of player to None
            #  Update DONE------------------

            direction_to_remove_opponent = (
                lambda r, c: "vertical" if (abs(r - recent_pos_row) != 0) else "horizontal")(nrow, ncol)

            is_reverse = (nrow < recent_pos_row or ncol < recent_pos_col)

            if direction_to_remove_opponent == "vertical":
                if not is_reverse:
                    for captured_player_row in range(recent_pos_row + 1, nrow,2 ):
                        # Clearing space in board
                        self.board_layout[(captured_player_row, ncol)] = None

                        # remove players

                        pl = self.fetch_player(captured_player_row, ncol)
                        pl.cur_row_pos = pl.cur_col_pos = None
                        self.player_list.remove(pl)

                else:
                    for captured_player_row in range(recent_pos_row - 1, nrow , -2):
                        self.board_layout[(captured_player_row, ncol)] = None

                        pl = self.fetch_player(captured_player_row, ncol)
                        self.player_list.remove(pl)

            elif direction_to_remove_opponent == "horizontal":

                if not is_reverse:
                    for captured_player_col in range(recent_pos_col + 1, ncol,2 ):
                        self.board_layout[(nrow, captured_player_col)] = None

                        pl = self.fetch_player(nrow, captured_player_col)
                        self.player_list.remove(pl)
                       # print("Player removed"+ str(pl.cur_row_pos) + str(pl.cur_col_pos))

                else:
                    for captured_player_col in range(recent_pos_col - 1, ncol, -2):
                        self.board_layout[(nrow, captured_player_col)] = None

                        pl = self.fetch_player(nrow, captured_player_col)

                        self.player_list.remove(pl)

            else:

                pass

            # After the board is updated with a new move, recalculate the value of SEF for this board instance
            # This also recalculates the possible play in the updated board.

            self.sef_value = self.calculate_sef()


        return True


    def is_game_over(self):
        """ This function checks whether a game is over or not, based on the values computed by sef.
            i.e., if either player has 0 moves for (1 or 2 or 3 possible hops), then game is over, and
            other player wins the game

        :return: tuple containing first value that indicates whether game is over or not, True-> game over ; False-> not over
        and second value, the color of the winner
        """
        # possible play for a board, is computed while invoking the calculate_sef method from Board class, which
        # in turn calls the total_available_move method
        # Strategy is to, check which players are available in the possible play, and if either of black or white
        # player does not exists in possible play, game is over and winner is another player

        safe_player=set()

        for each_move in self.possible_play:
            for k,v in each_move.items():
                r,c = k
                for each_player in self.player_list:
                    if each_player.cur_row_pos == r and each_player.cur_col_pos == c:
                        safe_player.add(each_player.player_type)
                        break

                break

        if "black" in safe_player and "white" in safe_player:

            return False, None

        else:
            winner = "black" if "black" in safe_player else "white"

            return True, winner


