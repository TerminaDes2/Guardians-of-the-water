import random, sys, constantes
sp1 = 0
sp2 = 1
sp3 = 2
sp4 = 3

def objetos(v1, v2, v3, v4):
    global sp1, sp2, sp3, sp4
    sp1 = v1
    sp2 = v2 
    sp3 = v3 
    sp4 = v4 

print("Se imprimen variables velocidad", sp1, sp2, sp3)
print(str(sys.argv))
def generar_circulos(num_circles, circle_radius):
    circles = []
    for i in range(num_circles):
        circle_x = random.uniform(circle_radius, constantes.ANCHURA_PANTALLA - circle_radius - 20)
        circle_y = random.uniform(260, constantes.ALTURA_PANTALLA - 40)
        circle_velocidad = asignar_velocidad(circle_y)
        circles.append([circle_x, circle_y, circle_velocidad])
    return circles
#sa
def generar_cuadrados(num_squares, square_size):
    squares = []
    for i in range(num_squares):
        square_x = random.uniform(0, constantes.ANCHURA_PANTALLA - square_size)
        square_y = random.uniform(265, constantes.ALTURA_PANTALLA - 40)
        square_velocidad = asignar_velocidad(square_y)
        square_flipped = -1  # 1 indica que no está volteado, -1 indica que está volteado
        squares.append([square_x, square_y, square_velocidad, square_flipped])
    return squares

def asignar_velocidad(y):
    if y >= 450:
        return random.uniform(sp1, sp2)
    elif y >= 300:
        return random.uniform(sp2, sp3)
    elif y >= 100:
        return random.uniform(sp3, sp4)
    return 0

#prueba Kris