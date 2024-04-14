import pygame
from constants import Colors


class Brush:
    sizes = [5, 15, 25]

    def __init__(self, screen):
        self.size = Brush.sizes[0]
        self.color = (0,0,0)
        self.screen = screen

    def handleEvents(self):
        keysPressed = pygame.key.get_pressed()        
        if(pygame.mouse.get_pressed()[0]):
            self.draw()


    def setBrushSize(self, size):
        self.size = size
    
    def setColor(self, color):
        self.color = color
    
    
    def draw(self):
        position = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, color=self.color, center=position, radius=10)