from typing import Any
import pygame

class Jugador(pygame.sprite.Sprite):

    def __init__(self,width,height,posX_init,posY_init,framelist,cant_frames):
        super().__init__()
        
        self.framesList = self.make_frame_list(framelist,width,height,(255,255,255))
        #Frame es una lista de sprites. La recorro y a cada elemento o sea imagen la transformo en surface, le aplico escala y trasparencia
        # y formo una nueva lista de surfaces pero para ir asginando al atributo imagen a medida que hay metodo de clase update.
        self.cant_frames = cant_frames     
        self.frame_anim_actual = 0
        # Cargo, transformo y aplico transparencia a las imagenes para tener un objeto surface para ponerle al atributo image
        '''self.frame_anim1 = pygame.image.load(frame1).convert()
        self.frame_anim1 = pygame.transform.scale(self.frame_anim1,(width,height))
        self.frame_anim1.set_colorkey((255,255,255))

        self.frame_anim2 = pygame.image.load(frame2).convert()
        self.frame_anim2 = pygame.transform.scale(self.frame_anim2,(width,height))
        self.frame_anim2.set_colorkey((255,255,255))'''
        
        # Le asigno la primera efecivamente a image y obtengo su objeto rect
        self.image = self.framesList[0]
        self.rect = self.image.get_rect() # Obtengo su tamaño y coordenadas y lo asigno al atributo rect.
        
        #Atributos de posiciones iniciales
        self.rect.x = posX_init #Seteo donde quiero sus posiciones iniciales.
        self.rect.y = posY_init

    
    def move_left(self,posiciones):
        self.rect.x -= posiciones

    def move_up(self,posiciones):
        self.rect.y -= posiciones
        

    def move_right(self,posiciones):
        self.rect.x += posiciones

    def move_down(self,posiciones):
        self.rect.y += posiciones

    def update(self):
        
        
        # Animacion
        self.cambiar_frame_anim()

        #Movimiento
 

    def cambiar_frame_anim(self):
        
        self.frame_anim_actual +=1

        if self.frame_anim_actual == self.cant_frames:
            self.frame_anim_actual = 0

        self.image = self.framesList[self.frame_anim_actual]
        #self.rect = self.image.get_rect()


    def make_frame_list(self,lista_frames,width,height,color_trasparencia):

        lista_sprites= []
        
        for i in range(0,len(lista_frames),1):
            surface = pygame.image.load(lista_frames[i]).convert()
            surface = pygame.transform.scale(surface,(width,height))
            surface.set_colorkey(color_trasparencia)
            surface.set_colorkey((0,0,0))

            lista_sprites.append(surface)
          
        return lista_sprites