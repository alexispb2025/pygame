import pygame

# Define las constantes
FPS = 60
COLOR_BG = (0, 0, 0)  # Fondo negro

pygame.init()

ancho = 880
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi primer juego")

# Crear el personaje como un rectángulo
jugador = pygame.Rect(400, 300, 50, 50)

# Variables de movimiento
mover_derecha = False
mover_izquierda = False
mover_arriba = False
mover_abajo = False

reloj = pygame.time.Clock()
run = True
while run:
    reloj.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    """Calcular el movimiento"""
    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = 5
    if mover_izquierda:
        delta_x = -5
    if mover_arriba:
        delta_y = -5
    if mover_abajo:
        delta_y = 5

    jugador.x += delta_x
    jugador.y += delta_y

    # Dibujar
    ventana.fill(COLOR_BG)  # Solo aquí
    pygame.draw.rect(ventana, (255, 0, 0), jugador)
    pygame.display.update()

pygame.quit()
