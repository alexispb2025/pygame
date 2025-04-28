import pygame
from personaje import Personaje 
player personaje (50, 50)

pygame.init()

ancho = 880
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("MI PRIMER JUEGO")

mi_personaje = Personaje(100, 100)

run = True
while run:

    player.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ventana.fill((0, 0, 0))  
   
