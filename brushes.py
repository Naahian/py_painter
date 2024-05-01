import pygame
from constants import Colors

class Brush:
    sizes = [5, 15, 25]

    def __init__(self, screen):
        self.size = Brush.sizes[0]
        self.color = Colors.black
        self.screen = screen

    def handleEvents(self):
        if(pygame.mouse.get_pressed()[0]):  #if left mouse button pressed
            self.draw()

    def setBrushSize(self, size):
        self.size = size
    
    def setColor(self, color):
        self.color = color
    
    def draw(self):
        position = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, color=self.color, center=position, radius=10)