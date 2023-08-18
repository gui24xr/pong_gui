from typing import Any
import pygame

class Bomba(pygame.sprite.Sprite):

    def __init__(self,posX_init,posY_init):
        super().__init__()
        
        self.sprites = [pygame.image.load("chars/bomb_izq.png"),pygame.image.load("chars/bomb_der.png")]
        self.frame = 0
        
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_rect()
        
        self.rect.x = posX_init
        self.rect.y = posY_init

        direccion_x = 1
        direccion_y = 1
        self.velocidad_x =  10
        self.velocidad_y = 10


    def update(self, tiempo):
        
        if tiempo % 20 == 0:
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y
    
    def cambiar_direccion_x(self,tiempo):
        if tiempo % 20 == 0:
            self.velocidad_x *=-1
            if(self.frame == 0): 
                self.frame = 1
                self.image = self.sprites[self.frame]
            elif (self.frame == 1): 
                self.frame = 0
                self.image = self.sprites[self.frame]

    
    def cambiar_direccion_y(self,tiempo):
        if tiempo % 20 == 0:
            self.velocidad_y*=-1
    



