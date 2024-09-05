import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pelota Movimiento")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
Ventana = (80, 180, 255)
cIELO = (120, 222, 255) 

fondo_cuerpo = [(48, 152), (152, 152), (177, 98), (23, 98)]
cuerpo = [(50, 150), (150, 150), (175, 100), (25, 100)]
points2 = [(80, 100), (160, 100), (140, 70), (110, 70)]
points_prueba = [(82, 99), (158 , 99), (139, 71), (111, 71)]
# Propiedades de la pelota
ball_radius = 20
ball_x = screen_width // 2
ball_y = 170
ball_speed = 5
speed = 5
ball_position = 10

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener todas las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover la pelota dependiendo de la tecla presionada
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        ball_y += ball_speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
       ball_y -= ball_speed

    
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cuerpo = [(x, y - speed) for x, y in cuerpo]
        fondo_cuerpo = [(x, y - speed) for x, y in fondo_cuerpo]
        points2 = [(x, y - speed) for x, y in points2]
        points_prueba = [(x, y - speed) for x, y in points_prueba]

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cuerpo = [(x, y + speed) for x, y in cuerpo]
        fondo_cuerpo = [(x, y + speed) for x, y in fondo_cuerpo]
        points2 = [(x, y + speed) for x, y in points2]
        points_prueba = [(x, y + speed) for x, y in points_prueba]

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cuerpo = [(x - speed, y) for x, y in cuerpo]
        fondo_cuerpo = [(x - speed, y) for x, y in fondo_cuerpo]
        points2 = [(x - speed, y) for x, y in points2]
        points_prueba = [(x - speed, y) for x, y in points_prueba]

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cuerpo = [(x + speed, y) for x, y in cuerpo]
        fondo_cuerpo = [(x + speed, y) for x, y in fondo_cuerpo]
        points2 = [(x + speed, y) for x, y in points2]
        points_prueba = [(x + speed, y) for x, y in points_prueba]

    # Evitar que la pelota salga de los bordes de la ventana
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    if ball_x + ball_radius > screen_width:
        ball_x = screen_width - ball_radius
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
    if ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius

    # Dibujar en la pantalla
    print(ball_speed, ball_radius, ball_x,ball_y)
    screen.fill(cIELO)
    pygame.draw.circle(screen, white, (ball_x-12, ball_y), ball_radius)
    pygame.draw.circle(screen, white, (ball_x+12, ball_y), ball_radius)
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    
    pygame.draw.polygon(screen, black,fondo_cuerpo)
    pygame.draw.polygon(screen, RED,cuerpo)
    pygame.draw.polygon(screen, black,points2)
    pygame.draw.polygon(screen, Ventana,points_prueba)
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de pygame
pygame.quit()
