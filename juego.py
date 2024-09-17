import pygame
import sys
import constantes
from barco import cargar_barco
from objetos import generar_circulos, generar_cuadrados
from funciones import draw_triangle, check_collision

# Inicializar Pygame
pygame.init()

screen = pygame.display.set_mode((constantes.ANCHURA_PANTALLA, constantes.ALTURA_PANTALLA))
pygame.display.set_caption("Guardians of the Water")

# Cargar el barco
barco, barco_rect = cargar_barco()

# Variables del barco y triángulo
velocidad = 5
movimiento_permitido = True
stop_time = 0
flip_horizontal = False
triangle_color = (0, 255, 0)
triangle_pos = [constantes.ANCHURA_PANTALLA // 2, 100]
triangle_size = 20
triangle_velocidad = (constantes.ALTURA_PANTALLA - 100) / 3
triangle_active = False
triangle_direction = 1
triangle_timer = 0
collision_detected = False

# Generar círculos y cuadrados
circles = generar_circulos(10, 10)
squares = generar_cuadrados(10, 15)

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el barco y ajustar la dirección
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and barco_rect.left > -84:
        barco_rect.x -= velocidad
        flip_horizontal = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and barco_rect.right < constantes.ANCHURA_PANTALLA + 84:
        barco_rect.x += velocidad
        flip_horizontal = True

    # Activar el triángulo cuando se presiona la barra espaciadora
    if keys[pygame.K_SPACE] and not triangle_active:
        movimiento_permitido = False
        velocidad = 0
        stop_time = pygame.time.get_ticks()
        triangle_active = True
        triangle_direction = 1  # El triángulo comienza a bajar
        triangle_timer = pygame.time.get_ticks()
        triangle_pos[1] = 100  # Posición inicial del triángulo
        collision_detected = False

    # Mover el triángulo si está activo
    if triangle_active:
        time_passed = (pygame.time.get_ticks() - triangle_timer) / 1000  # Tiempo en segundos

        if not collision_detected:  # Movimiento normal sin colisión
            if triangle_direction == 1:  # Bajando
                triangle_pos[1] += triangle_velocidad * clock.get_time() / 1000
                if triangle_pos[1] >= constantes.ALTURA_PANTALLA - triangle_size:
                    triangle_direction = -1  # Comienza a subir
                    triangle_timer = pygame.time.get_ticks()
            elif triangle_direction == -1:  # Subiendo
                triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000
                if triangle_pos[1] <= 100:
                    triangle_active = False  # Termina el ciclo
                    triangle_pos[1] = 100

        if collision_detected:  # Si se detecta una colisión
            triangle_direction = -1  # Asegúrate de que siempre suba tras colisión
            triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000  # Subir
            if triangle_pos[1] <= 100:  # Si ya ha subido completamente
                triangle_active = False  # Detener el triángulo
                collision_detected = False  # Resetear la colisión para futuros movimientos

        # Verificar colisión con círculos o cuadrados
        for circle in circles:
            if check_collision(triangle_pos, triangle_size, (circle[0], circle[1]), 10 * 2):
                collision_detected = True
                triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir

        for square in squares:
            if check_collision(triangle_pos, triangle_size, (square[0], square[1]), 15):
                collision_detected = True
                triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir

    # Dibujar el fondo
    screen.fill(constantes.CIELO)

    # Dibujar el barco, con o sin flip según corresponda
    if flip_horizontal:
        barco_flipped = pygame.transform.flip(barco, True, False)
        screen.blit(barco_flipped, barco_rect)
    else:
        screen.blit(barco, barco_rect)

    # Dibujar el mar
    pygame.draw.polygon(screen, constantes.MARCOLOR, constantes.MAR)

    # Mover y dibujar los círculos
    for circle in circles:
        circle[0] += circle[2]
        if circle[0] - 10 > constantes.ANCHURA_PANTALLA or circle[0] + 10 < 0:
            circle[2] *= -1
        pygame.draw.circle(screen, constantes.RED, (int(circle[0]), int(circle[1])), 10)

    # Mover y dibujar los cuadrados
    for square in squares:
        square[0] += square[2]
        if square[0] + 15 > constantes.ANCHURA_PANTALLA or square[0] < 0:
            square[2] *= -1
        pygame.draw.rect(screen, constantes.BLACK, (square[0], square[1], 15, 15))

    # Dibujar el triángulo si está activo
    if triangle_active:
        draw_triangle(screen, triangle_color, triangle_pos, triangle_size)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la tasa de frames a 60
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
sys.exit()
