
class Player:

    def __init__(self, row_pos, col_pos, pid, color):
        """This method initializes the player object
        Each player has a state of its own which includes the row position, the column position, a unique pid and a color
        Returns: A player object that is instantiated by the caller"""
        self.cur_row_pos=row_pos
        self.cur_col_pos=col_pos
        self.player_id=pid
        self.player_type=color


    def can_move(self, new_pos):
        """ Input: new position of the player
        This methods validates whether the new input position for a player is  a valid move or not in the board, but
        it does not conform whether the cell is empty where the player want to move. Availability of cell to move,
        is implemented in Board class, method "is_empty_cell".  Together , with the is_empty_cell method from Board Class
        we can finally conclude, whether player is movable and we can update the gameplay.
        Returns: Boolean value, True or False"""

        new_row_pos, new_col_pos=new_pos # new_pos is a tuple that is passed into this method


        if (new_row_pos in range (0,7) and new_col_pos in range (0,7)): #Check the bound, the new row and column should not cross the board

            # |new position -old position|%2==0 determines correct move in both horizontal and vertical direction

            row_jump_distance=abs(new_row_pos-self.cur_row_pos)
            col_jump_distance=abs(new_col_pos-self.cur_col_pos)

            # row_jump_distance or column_jump_distance !=0 verifies that the move is not in the same place as current

            if ( row_jump_distance !=0 and  row_jump_distance % 2 == 0 and self.cur_col_pos == new_col_pos) or \
                        (self.cur_row_pos == new_row_pos and col_jump_distance!=0 and col_jump_distance % 2 == 0):

                return True

            else:

                return False
        else:

            return False











