from typing import Any
import pygame

class Pared(pygame.sprite.Sprite):

    def __init__(self,width,height,posX_init,posY_init,ladrillo):
        super().__init__()
        
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect()
        
        self.rect.x = posX_init
        self.rect.y = posY_init
        
        '''
        self.image.fill((250,230,0))
        pygame.draw.circle(self.image, (154,205,50),(50,50), 20)
        foto = pygame.image.load("chars/pelota.png")
        self.image.blit(foto,(20,20))
        '''
        self.image.fill((250,230,0))
        #Dibujo ladrillos hasta terminar ancho.
        imagen_ladrillo = (pygame.image.load(ladrillo)) #cargue la imagen en una variable para sacarle info
        
        for i in range(0,width,imagen_ladrillo.get_width()):
            self.image.blit(imagen_ladrillo,(i,0))
        for j in range(0,height,imagen_ladrillo.get_height()):
            self.image.blit(imagen_ladrillo,(0,j))

    
    
    



