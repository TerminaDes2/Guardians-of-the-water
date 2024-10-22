import random
import pygame
import constantes

def generar_circulos(num_circles, circle_radius):
    circles = []
    for i in range(num_circles):
        circle_x = random.uniform(circle_radius, constantes.ANCHURA_PANTALLA - circle_radius)
        circle_y = random.uniform(260, constantes.ALTURA_PANTALLA - 40)
        circle_velocidad = asignar_velocidad(circle_y)
        circles.append([circle_x, circle_y, circle_velocidad])
    return circles

def generar_cuadrados(num_squares, square_size):
    squares = []
    for i in range(num_squares):
        square_x = random.uniform(0, constantes.ANCHURA_PANTALLA - square_size)
        square_y = random.uniform(260, constantes.ALTURA_PANTALLA - square_size)
        square_velocidad = asignar_velocidad(square_y)
        square_flipped = 1  # 1 indica que no está volteado, -1 indica que está volteado
        squares.append([square_x, square_y, square_velocidad, square_flipped])
    return squares

def asignar_velocidad(y):
    if y >= 450:
        return random.uniform(2, 3)
    elif y >= 300:
        return random.uniform(1, 2)
    elif y >= 100:
        return random.uniform(0, 1)
    return 0
