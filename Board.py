from Player import Player  # Import the players class which defines the players attributes and behavior


class Board:
    # instance variable board layout is a 2-dimensional matrix having range (00,77)
    # board_layout example : { (3,4): pb12, }. This means at position row=3 and column=4, there is a black player with id of 12
    # We declare board_layout as instance variable (i.e, one board/object), because only one board view can exist at a particular time (i.e, state)
    # pb and pw are naming conventions for black players and white players respectively.
    # Naming convention for board_id would be bl(level no followed by ascending number)
    # Initially, all the players in the board are "None" (or equivalently, null). We'll initialize them in following section



    def __init__(self, board_id, player_list):
        """This method initializes a board object. Each board has 64 players
        Input: A list of Player objects. Initially 62, but as game continues, the player count would decrease.
               Board_id which uniquely identifies the board.
        Returns: A board object with positioned players that is instantiated by the caller."""

        self.board_id = board_id
        self.player_list=player_list

        self.board_layout = {(x, y): None for x in range(8) for y in range(8)}

        # TODO create static evaluation function and implemnet gameEngine in another module

        for individual_player in player_list:

            player_row=individual_player.cur_row_pos
            player_col=individual_player.cur_col_pos
            player_id=individual_player.player_id

            #Get the row and column position on the board, and place the individual players one after another

            self.board_layout[(player_row,player_col)]=player_id


    def total_available_moves_for_players(self):
        """This is the Static Evaluation Function which determines the game strategy
        We captures the available moves for black and white players, and draw a tree based on these values of SEF
        Input: Board Object (current)
        Returns: total black moves, total white moves"""

        black_players_count = 0
        white_players_count = 0

        for fighter in self.player_list:


            for cells_row_in_board in range(0,7):           # Loop iterates through (0,0 to 7,7)
                for cells_col_in_board in range (0,7):

                    if (fighter.can_move(cells_row_in_board,cells_col_in_board) and self.is_empty_cell(cells_row_in_board,cells_col_in_board)):

                        player_count_to_increase=fighter.player_type

                        if player_count_to_increase=="black":
                            black_players_count += 1

                        elif player_count_to_increase=="white":
                            white_players_count += 1

        return black_players_count,white_players_count

    def is_empty_cell(self, row,col):
        """This method determines whether a particular cell in a board in empty
        Input: Cell Number i.e., in terms of row and column
        Returns: boolean value, True or False"""

        if self.board_layout[(row,col)] is None:
            return True

        else:
            return False


    def update_board(self, nrow, ncol, to_be_updated_player):
        """Updates the board into another state
        Input: new_row, new_column for a player to move
                Player object (i.e., a player) to be updated . Note, only 1 update at a time
        Returns: same Board object with the implemented moves with respect to new row and column"""

        recent_pos_row= to_be_updated_player.cur_row_pos
        recent_pos_col= to_be_updated_player.cur_col_pos
        #player_id = to_be_updated_player.player_id TODO Redundant player information, not needed here, remove later

        #Check whether player can move and the cell where it is moving is empty or not
        if (to_be_updated_player.can_move((nrow,ncol)) and self.is_empty_cell(nrow,ncol)):

            #Update the new position for that player
            to_be_updated_player.cur_row_pos=nrow
            to_be_updated_player.cur_col_pos=ncol

            # Change the state of the board

            self.board_layout[(nrow,ncol)] = to_be_updated_player.player_id

            # Clear the earlier state of player in the board i.e, update to None
            self.board_layout[(recent_pos_row,recent_pos_col)] = None

            #Also remove any opponent in the way

            direction_to_remove_opponent=lambda nrow,ncol: "vertical" if (abs(nrow-recent_pos_row)) else "horizontal"

            if direction_to_remove_opponent == "vertical":
                for captured_player_row in range(recent_pos_row+1, nrow-1):
                    self.board_layout[(captured_player_row, ncol)]=None

            elif direction_to_remove_opponent == "horizontal":

                for captured_player_col in range(recent_pos_col+1, ncol-1):
                    self.board_layout[(nrow,captured_player_col)] = None

            else:
                pass

            return























