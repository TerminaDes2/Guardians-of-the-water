import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guardians of the water")

black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
Ventana = (80, 180, 255)
Cielo = (120, 222, 255) 
Mar = (32,112,225)

mar = [(800, 600), (0, 600), (0, 178), (800, 178)]

barco = pygame.image.load("barco.png")

barco = pygame.transform.scale(barco, (barco.get_width() * 4, barco.get_height() * 4))

barco_rect = barco.get_rect()
barco_rect.center = (screen_width // 2, 172)

speed = 5
movement_allowed = True
stop_time = 0
flip_horizontal = False

clock = pygame.time.Clock()

circles = []
num_circles = 10
circle_radius = 10
squares = []
num_squares = 10
square_size = 15

for i in range(num_circles):
    circle_x = random.uniform(circle_radius, screen_width - circle_radius)
    circle_y = random.uniform(screen_height // 3, screen_height - circle_radius)
    if circle_y >= 100:
        circle_speed = random.uniform(0,2)  
    if circle_y >= 300:
        circle_speed = random.uniform(3,5)
    if circle_y >= 450: 
        circle_speed = random.uniform(6,8)   
    circles.append([circle_x, circle_y, circle_speed])

for i in range(num_squares):
    square_x = random.uniform(0, screen_width - square_size)
    square_y = random.uniform(screen_height // 3, screen_height - square_size)
    if square_y >= 100:
        square_speed = random.uniform(0,2)  
    if square_y >= 300:
        square_speed = random.uniform(3,5)
    if square_y >= 450: 
        square_speed = random.uniform(6,8)   
    squares.append([square_x, square_y, square_speed])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not movement_allowed:
        if pygame.time.get_ticks() - stop_time >= 4000:
            movement_allowed = True
            speed = 5

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT] and barco_rect.left > -84:
        barco_rect.x -= speed
        flip_horizontal = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and barco_rect.right < screen_width + 84:
        barco_rect.x += speed
        flip_horizontal = True
    if keys[pygame.K_SPACE]:
        movement_allowed = False
        speed = 0
        stop_time = pygame.time.get_ticks()

    screen.fill(Cielo)

    if flip_horizontal:
        barco_flipped = pygame.transform.flip(barco, True, False)
        screen.blit(barco_flipped, barco_rect)
    else:
        screen.blit(barco, barco_rect)
    
    pygame.draw.polygon(screen, Mar, mar)
    
    for circle in circles:
        circle[0] += circle[2]  
        if circle[0] - circle_radius > screen_width or circle[0] + circle_radius < 0:
            circle[2] *= -1  

        pygame.draw.circle(screen, RED, (int(circle[0]), int(circle[1])), circle_radius)

    for square in squares:
        square[0] += square[2]  
        if square[0] + square_size > screen_width or square[0] < 0:
            square[2] *= -1  

        pygame.draw.rect(screen, black, (square[0], square[1], square_size, square_size))

    pygame.draw.circle(screen, white, (70-20, 60), 20)
    pygame.draw.circle(screen, white, (70+22, 60), 20)
    pygame.draw.circle(screen, white, (70, 60), 20)
    pygame.draw.circle(screen, white, (300-20, 60+10), 20)
    pygame.draw.circle(screen, white, (300+22, 60), 20)
    pygame.draw.circle(screen, white, (300-40, 60), 20)
    pygame.draw.circle(screen, white, (300, 60), 20)
    pygame.display.flip()

    pygame.time.Clock().tick(120)

pygame.quit()
sys.exit()
