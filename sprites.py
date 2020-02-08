import pygame

class playerSprite():

    def __init__(self,img, target_position):
        """create and initialize all the players"""

        self.image=img
        self.target=target_position
        self.current=target_position

    def update(self):
        """Update the position of the sprites"""

        return

    def draw(self,target_surface):

        target_surface.blit(self.image,self.current)


