import pygame
from brushes import Brush
from constants import *
from toolbar import Toolbar


pygame.init()
screen = pygame.display.set_mode(Default.resolution)

#load initials
clock = pygame.time.Clock()
screen.fill(Colors.white)
brush = Brush(screen)
toolbar = Toolbar(screen, brush)


running = True
while(running):
    time_delta = clock.tick(Default.fps)/1000.0

    for event in pygame.event.get():    
        brush.handleEvents()
        toolbar.handleEvents(event)
        

        if(event.type == pygame.QUIT):
            running = False     


    toolbar.draw_ui(screen)
    toolbar.update(time_delta)
    pygame.display.update()

pygame.quit()