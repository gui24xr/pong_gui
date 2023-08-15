from typing import Any
import pygame

class Bomba(pygame.sprite.Sprite):

    def __init__(self,posX_init,posY_init):
        super().__init__()
        
        self.image = pygame.image.load("chars/bomb_izq.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = posX_init
        self.rect.y = posY_init



    
    
    



