import pygame,sys
from jugador import Jugador
from paredes import Pared
from bomba import Bomba



def iniciar_pantalla_juego(width,height,titulo):
    
    pygame.init()
    pantalla = pygame.display.set_mode((width,height))
    pygame.display.set_caption(titulo)
    return pantalla

# COnstantes
pantalla_width = 1160
pantalla_height = 700
paletas_height = 100
paletas_width = 100
paleta1_spritelist = ["chars/jugador1.png","chars/jugador2.png"]
paleta2_spritelist = ["chars/jugador3.png","chars/jugador4.png"]
pared_espesor = 40
techo_height = 40
piso_height = 40

pantalla_juego = iniciar_pantalla_juego(1160,700,"Mi Juego")
clock =  pygame.time.Clock()
sprites_draw = pygame.sprite.Group()
#---------------------
techo = Pared(pantalla_width,techo_height,0,0,"chars/block_techo.png")
piso = Pared(pantalla_width,pared_espesor,0,pantalla_height-piso_height,"chars/piso.png")
pared_izq = Pared(pared_espesor,pantalla_height,0,0,"chars/block_pared_izq.png")
pared_der = Pared(pared_espesor,pantalla_height,pantalla_width-pared_espesor,0,"chars/block_pared_der.png")
#----------------------------------------

bomba = Bomba(pantalla_width/2,pantalla_height/2)
jugador1 = Jugador(paletas_height,paletas_width,pared_espesor,(pantalla_juego.get_height() / 2)-paletas_height/2,paleta1_spritelist,len(paleta1_spritelist))
jugador2 = Jugador(paletas_height,paletas_width,pantalla_juego.get_width()-pared_espesor*3.5,pantalla_juego.get_height() / 2-paletas_height/2,paleta2_spritelist,len(paleta2_spritelist))


sprites_draw.add(bomba,jugador1,jugador2,piso ,techo,pared_izq,pared_der)

#Colisiones

dict_colision = pygame.sprite.spritecollide(jugador1,[techo],False)
    
game_end = False

while (not game_end):

    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN or event.type == pygame.KEYDOWN):

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_z:
                jugador1.move_down(12)
            if event.key == pygame.K_w:
                jugador1.move_up(12)
            if event.key == pygame.K_a:
                jugador1.move_left(12)
            if event.key == pygame.K_s:
                jugador1.move_right(12)
            if event.key == pygame.K_DOWN:
                jugador2.move_down(12)
            if event.key == pygame.K_UP:
                jugador2.move_up(12)
            if event.key == pygame.K_LEFT:
                jugador2.move_left(12)
            if event.key == pygame.K_RIGHT:
                jugador2.move_right(12)


    
    pantalla_juego.fill((112,202,238))
    sprites_draw.update()
    sprites_draw.draw(pantalla_juego)

    grupo = pygame.sprite.Group(jugador2)
    collided = pygame.sprite.spritecollide(jugador1, grupo, True)
    if collided: print("Colision")


    pygame.display.flip()
   
     