import pygame
import math

def place_palyers(the_board, square_size):
    pass





def draw_board(the_board):
    """ Draw a konane board with black and white players, from the_board. """

    pygame.init()
    colors = [(245,222,179), (205,133,63)]    # Set up colors [wheat, peru]

    n = int(math.sqrt(len(the_board)))     # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))


    black_player = pygame.image.load("black.png")
    white_player = pygame.image.load("white.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered
    black_player_offset = (sq_sz - black_player.get_width()) // 2
    white_player_offset = (sq_sz - white_player.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # draw the players, white players occupy even space, and black players occupy odd space
        for (col, row) in the_board:

            if (row+col)%2==1:
                surface.blit(black_player,
                             (col * sq_sz + black_player_offset, row * sq_sz + black_player_offset))

            else:
                surface.blit(white_player,
                       (col*sq_sz+white_player_offset,row*sq_sz+white_player_offset))



        pygame.display.flip()


    pygame.quit()

if __name__=="__main__":

    intial_config=[(x,y) for x in range(8) for y in range(8)] #create a matrix of size 8*8
    draw_board(intial_config) #Index of the list represents column, and the value represents row
