import pygame

pygame.init()

ancho = 880
alto = 600

# CORREGIDO AQUÍ
ventana = pygame.display.set_mode((ancho, alto))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

