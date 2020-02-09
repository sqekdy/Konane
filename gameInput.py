import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    display_color_maroon=(176,48,96)
    display_color_yellow=(255,255,224)
    name = ""
    font = pygame.font.Font(None, 27)
    text=font.render('Welcome to Konane!  Please choose a color (B or W)',True, display_color_maroon,display_color_yellow)

    textbox=text.get_rect()


    while True:

        screen.fill((0, 0, 0))
        textbox.center = screen.get_rect().center
        screen.blit(text, textbox)
        pygame.display.flip()


        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = name
            elif evt.type == QUIT:
                return

            user_selection_color=font.render(" Your choice: {}".format(name), True,display_color_maroon,display_color_yellow)
            screen.blit(user_selection_color, (250,400))
    pygame.display.update()







name()