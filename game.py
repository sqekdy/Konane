import pygame
import math

class boardUI:

    def __init__(self, the_board):

        pygame.init()
        self.colors = [(245, 222, 179), (205, 133, 63)]  # Set up colors [wheat, peru]

        # TODO This gives error at later stage, as size of board shrinks and board size is pruned
        # Use static value as of now, and figure out to dynamically create the board.
        # n = int(math.sqrt(len(the_board)+2))     # This is an NxN chess board, +2 because initially 2 players are removed
        self.n = 8
        self.surface_sz = 480  # Proposed physical surface size.
        self.sq_sz = self.surface_sz // self.n  # sq_sz is length of a square.
        self.surface_sz = self.n * self.sq_sz  # Adjust to exactly fit n squares.

        # Create the surface of (width, height), and its window.
        self.screen = pygame.display.set_mode((self.surface_sz, self.surface_sz))

        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        self.eve = None

        all_players = []

        self.black_player = pygame.image.load("black.png")
        self.white_player = pygame.image.load("white.png")

        # Use an extra offset to centre the ball in its square.
        # If the square is too small, offset becomes negative,
        #   but it will still be centered
        self.black_player_offset = (self.sq_sz - self.black_player.get_width()) // 2
        self.white_player_offset = (self.sq_sz - self.white_player.get_width()) // 2

        for row in range(self.n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(self.n):  # Run through cols drawing squares
                the_square = (col * self.sq_sz, row * self.sq_sz, self.sq_sz, self.sq_sz)
                self.surface.fill(self.colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2


        # draw the players, white players occupy even space, and black players occupy odd space
        for (col, row) in the_board:

            if (row + col) % 2 == 0:
                self.surface.blit(self.black_player,
                             (col * self.sq_sz + self.black_player_offset, row * self.sq_sz + self.black_player_offset))

            else:
                self.surface.blit(self.white_player,
                             (col * self.sq_sz + self.white_player_offset, row * self.sq_sz + self.white_player_offset))

        self.screen.blit(self.surface, (0, 0))

        # while 1:
        #     self.eve = pygame.event.poll()
        #     if self.eve.type == pygame.QUIT:
        #         pygame.quit()
        #         break

        pygame.display.flip()



    def take_input(self):
        """ Draw a konane board with black and white players, from the_board. """

        print("reached here")
        hover = False
        selection = False
        count_selection = 0
        selected_cell= None

        move_coordinate = list()

        while True:

            # Look for an event from keyboard, mouse, etc.
            self.eve = pygame.event.poll()
            if self.eve.type == pygame.QUIT:
                pygame.quit()
                break

            if self.eve.type == pygame.MOUSEMOTION:
                hover = True

            if self.eve.type == pygame.MOUSEBUTTONDOWN:
                selection = True

            # Draw a fresh background (a blank chess board)


            if hover:
                pos = pygame.mouse.get_pos()
                col_pos, row_pos = pos[0] // self.sq_sz, pos[1] // self.sq_sz
                # print(col_pos, row_pos)

                self.screen.blit(self.surface, (0, 0))

                pygame.draw.rect(self.screen, (255, 0, 0), (col_pos * self.sq_sz, row_pos * self.sq_sz, self.sq_sz,
                                                            self.sq_sz), 5)

                pygame.display.flip()

            if selection and count_selection < 2:
                count_selection += 1
                pos = pygame.mouse.get_pos()

                # print(selected_cell.left, selected_cell.top)

                selection = False

                col_pos, row_pos = pos[0] // self.sq_sz, pos[1] // self.sq_sz

                move_coordinate.extend([row_pos, col_pos])


                selected_cell= pygame.draw.rect(self.surface, (50, 205, 50), (col_pos * self.sq_sz, row_pos * self.sq_sz,
                                                               self.sq_sz, self.sq_sz), 5)

                pygame.display.flip()

            if count_selection == 2:
                return move_coordinate



    def draw_board (self, updated_board):

        for row in range(self.n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(self.n):  # Run through cols drawing squares
                the_square = (col * self.sq_sz, row * self.sq_sz, self.sq_sz, self.sq_sz)
                self.surface.fill(self.colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        for (col, row) in updated_board:

            if (row + col) % 2 == 0:
                self.surface.blit(self.black_player,
                             (col * self.sq_sz + self.black_player_offset, row * self.sq_sz + self.black_player_offset))

            else:
                self.surface.blit(self.white_player,
                             (col * self.sq_sz + self.white_player_offset, row * self.sq_sz + self.white_player_offset))

        self.screen.blit(self.surface, (0, 0))

        pygame.display.flip()



# if __name__=="__main__":
#
#     intial_config=[(x,y) for x in range(8) for y in range(8)] #create a matrix of size 8*8
#     draw_board(intial_config) #Index of the list represents column, and the value represents row
