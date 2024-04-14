import pygame
import pygame_gui
from constants import Default, Colors

class Toolbar(pygame_gui.UIManager):
    selectedColor = None
    def __init__(self, screen, brush):
        super().__init__(Default.resolution, "./theme.json") 
        self.screen = screen
        self.brush = brush
        self.selectedColor = brush.color 

        self.redPallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((130,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_red",
        )
        self.greenPallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((160,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_green",
        )
        self.bluePallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((190,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_blue",
        )
        self.purplePallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((220,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_purple",
        )
        self.cyanPallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((250,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_cyan",
        )
        self.yellowPallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((280,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_yellow",
        )
        self.blackPallete = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((310,0), (30,30)),
            manager=self,
            text="",
            object_id="#button_black",
        )
        self.clearButton = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((360,0), (100,30)),
            text = 'ERASE ALL',
            object_id="#button_white",
            manager=self,
        )
 

        
    
    def handleEvents(self, event):
        self.process_events(event)
        self._buttonEvent(event)

    def _buttonEvent(self, event):
        if(event.type == pygame_gui.UI_BUTTON_PRESSED):
            if(event.ui_element == self.clearButton): 
                self.screen.fill(Colors.white)

            elif(event.ui_element == self.redPallete): 
                self.brush.setColor(Colors.red)
            
            elif(event.ui_element == self.greenPallete): 
                self.brush.setColor(Colors.green)
            
            elif(event.ui_element == self.bluePallete): 
                self.brush.setColor(Colors.blue)
            
            elif(event.ui_element == self.yellowPallete): 
                self.brush.setColor(Colors.yellow)
            
            elif(event.ui_element == self.purplePallete): 
                self.brush.setColor(Colors.purple)
            
            elif(event.ui_element == self.cyanPallete): 
                self.brush.setColor(Colors.cyan)
            
            elif(event.ui_element == self.blackPallete): 
                self.brush.setColor(Colors.black)
            
                    
    
        



