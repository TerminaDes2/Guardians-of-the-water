import random
import constantes

def generar_circulos(num_circles, circle_radius):
    circles = []
    for i in range(num_circles):
        circle_x = random.uniform(circle_radius, constantes.ANCHURA_PANTALLA - circle_radius)
        circle_y = random.uniform(constantes.ALTURA_PANTALLA // 3, constantes.ALTURA_PANTALLA - circle_radius)
        circle_velocidad = asignar_velocidad(circle_y)
        circles.append([circle_x, circle_y, circle_velocidad])
    return circles

def generar_cuadrados(num_squares, square_size):
    squares = []
    for i in range(num_squares):
        square_x = random.uniform(0, constantes.ANCHURA_PANTALLA - square_size)
        square_y = random.uniform(constantes.ALTURA_PANTALLA // 3, constantes.ALTURA_PANTALLA - square_size)
        square_velocidad = asignar_velocidad(square_y)
        squares.append([square_x, square_y, square_velocidad])
    return squares

def asignar_velocidad(y):
    if y >= 450:
        return random.uniform(6, 8)
    elif y >= 300:
        return random.uniform(3, 5)
    elif y >= 100:
        return random.uniform(0, 2)
    return 0
