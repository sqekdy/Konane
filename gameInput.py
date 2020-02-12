import pygame
from pygame.locals import *
import time


def handle_user_input():

    input_from_user=""

    while True:

        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    input_from_user += evt.unicode
                elif evt.key == K_BACKSPACE:
                    input_from_user = input_from_user[:-1]
                elif evt.key == K_RETURN:


                    #TODO Use the following code in message_printer
                    # msg = ("Black plays first! Your selection is: {}".format(input_from_user))
                    # choice_sel_block = font.render(msg, True, (255, 255, 255))
                    # screen.blit(choice_sel_block, (120, 450))
                    # pygame.display.update()
                    # time.sleep(5)

                    # TODO pop up the main game screen and handel the code there.
                    return input_from_user

            elif evt.type == QUIT:
                return


def message_printer(screen):

    screen.fill((0, 0, 0))
    textbox.center = screen.get_rect().center
    screen.blit(text, textbox)
    pygame.display.update()



def name():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    display_color_maroon=(176,48,96)   #color for the text
    display_color_yellow=(255,255,224)  #color for the textbox
    font = pygame.font.Font(None, 27)
    text=font.render('Welcome to Konane!  Please choose a color (B or W)',True, display_color_maroon,display_color_yellow)
    textbox=text.get_rect()
    block = font.render("Your choice is :{}".format(name), True, (255, 255, 255))
    screen.blit(block, (150,350))
    pygame.display.flit()


name()