import pygame
import sys
import constantes
from barco import cargar_barco
from objetos import generar_circulos, generar_cuadrados

# Inicializar Pygame
pygame.init()

screen = pygame.display.set_mode((constantes.ANCHURA_PANTALLA, constantes.ALTURA_PANTALLA))
pygame.display.set_caption("Guardians of the Ocean")
# Cargar el barco
barco, barco_rect = cargar_barco()

fondo, fondo_rect = cargar_barco()

#dibujo barra de vida
alt_x = 14
alt_y = 84
divisible = 84 - 14

# Variables del barco y triángulo
velocidad = 5
movimiento_permitido = True
stop_time = 0
flip_horizontal = False
triangle_color = (0, 255, 0)
triangle_pos = [constantes.ANCHURA_PANTALLA // 2, 100]
triangle_size = 20
triangle_velocidad = 300
triangle_active = True
triangle_movement = False
triangle_direction = 1
triangle_timer = 0
collision_detected = False
colisiones_activas = True

#Cantidad de animales que puedes agarrar para perder
pierdes = 5

# Variables del contador
start_ticks = pygame.time.get_ticks()  # Tiempo inicial
cuadrados_agarrados = 0  # Contador de cuadrados agarrados
circulos_agarrados = 0  # Contador de circulos agarrados
tiempo_limite = 120  # Minutos en segundos

# Generar círculos y cuadrados
circles = generar_circulos(10, 10)
squares = generar_cuadrados(10, 15)

#copia la cantidad de elementos en la lista circles
circulos_eliminables = len(circles)

# Función para verificar colisiones
def check_collision(triangle_pos, triangle_size, obj_pos, obj_size):
    if flip_horizontal:
        triangle_rect = pygame.Rect(barco_rect.left - triangle_size + 40, triangle_pos[1] + 20, triangle_size * 2, triangle_size)
        print(triangle_rect)
    else:  
        triangle_rect = pygame.Rect(barco_rect.right - triangle_size - 40, triangle_pos[1] + 20, triangle_size * 2, triangle_size)
        print(triangle_rect)

    obj_rect = pygame.Rect(obj_pos[0], obj_pos[1], obj_size, obj_size)
    return triangle_rect.colliderect(obj_rect)

# Cargar la imagen de fondo y escalarla
fondo = pygame.image.load("fondo22.png")
fondo_escalado = pygame.transform.scale(fondo, (800, 600))

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar si el tiempo se agotó
    segundos_transcurridos = (pygame.time.get_ticks() - start_ticks) / 1000
    tiempo_restante = tiempo_limite - segundos_transcurridos
    if tiempo_restante <= 0 or cuadrados_agarrados >= pierdes :
        # Mostrar mensaje de "Perdiste"
        font = pygame.font.Font(None, 74)
        texto_perdiste = font.render("Sigue intentando", True, (255, 0, 0))
        screen.blit(texto_perdiste, (constantes.ANCHURA_PANTALLA // 2 - 100, constantes.ALTURA_PANTALLA // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        
    if circulos_agarrados == circulos_eliminables:
        font = pygame.font.Font(None, 74)
        texto_perdiste = font.render("Ganaste", True, (255, 215, 0))
        screen.blit(texto_perdiste, (constantes.ANCHURA_PANTALLA // 2 - 100, constantes.ALTURA_PANTALLA // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Dibuja el fondo escalado
    screen.blit(fondo_escalado, (0, 0))

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el barco y ajustar la dirección
    if keys[pygame.K_a] and triangle_movement == False and barco_rect.left > -24 or keys[pygame.K_LEFT] and triangle_movement == False and barco_rect.left > -24:
        barco_rect.x -= velocidad
        flip_horizontal = True
    if keys[pygame.K_d] and triangle_movement == False and barco_rect.right < constantes.ANCHURA_PANTALLA + 24 or keys[pygame.K_RIGHT] and triangle_movement == False and barco_rect.right < constantes.ANCHURA_PANTALLA + 24:
        barco_rect.x += velocidad
        flip_horizontal = False

    # Activar el triángulo cuando se presiona la barra espaciadora
    if keys[pygame.K_SPACE] and triangle_movement == False or keys[pygame.K_DOWN] and triangle_movement == False:
        triangle_movement = True
        triangle_direction = 1  # El triángulo comienza a bajar
        triangle_timer = pygame.time.get_ticks()
        triangle_pos[1] = 100  # Posición inicial del triángulo
        collision_detected = False
        movimiento_permitido = False
        velocidad = 0

    # Mover el triángulo si está activo
    if triangle_movement:
        time_passed = (pygame.time.get_ticks() - triangle_timer) / 1000  # Tiempo en segundos

        if not collision_detected:  # Movimiento normal sin colisión
            if triangle_direction == 1:  # Bajando
                triangle_pos[1] += triangle_velocidad * clock.get_time() / 1000
                if triangle_pos[1] >= constantes.ALTURA_PANTALLA - triangle_size:
                    colisiones_activas = False  # Desactivar colisiones al llegar al fondo
                    triangle_direction = -1  # Comienza a subir
                    triangle_timer = pygame.time.get_ticks()
            elif triangle_direction == -1:  # Subiendo
                triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000
                if triangle_pos[1] <= 100:
                    triangle_movement = False
                    velocidad = 0
                    triangle_movement = False  # Termina el ciclo
                    triangle_pos[1] = 100
                    movimiento_permitido = True
                    velocidad = 5
                    colisiones_activas = True  # Activar colisiones al llegar a su altura original

        if collision_detected:  # Si se detecta una colisión
            colisiones_activas = False  # Desactivar colisiones al colisionar con un objeto
            triangle_direction = -1  # Asegúra de que siempre suba tras colisión
            triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000  # Subir
            if triangle_pos[1] <= 100:  # Si ya ha subido completamente
                movimiento_permitido = True
                velocidad = 5
                triangle_movement = False  # Detener el triángulo
                collision_detected = False  # Resetear la colisión para futuros movimientos
                colisiones_activas = True  # Activar colisiones al colisionar con un objeto

        # Verifica la colisión con círculos o cuadrados solo si las colisiones están activas
        if colisiones_activas:
            for circle in circles:
                if check_collision(triangle_pos, triangle_size, (circle[0], circle[1]), 10 * 2):
                    collision_detected = True
                    triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir
                    circles.remove(circle) #Elimina el circulo golpeado
                    circulos_agarrados += 1  # Aumentar contador de circulos agarrados
                    colisiones_activas = False  # Desactivar colisiones
            for square in squares:
                if check_collision(triangle_pos, triangle_size, (square[0], square[1]), 15):
                    collision_detected = True
                    triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir
                    squares.remove(square) #Elimina el cuadrado golpeado
                    cuadrados_agarrados += 1  # Aumentar contador de cuadrados agarrados
                    colisiones_activas = False  # Desactivar colisiones
                    alt_x += divisible / (pierdes - 1)
                    alt_y -= divisible / (pierdes - 1)

    # Dibuja el fondo
    #screen.fill(constantes.CIELO)
    #pygame.draw.polygon(screen, constantes.MARCOLOR, constantes.MAR)
    #screen.blit(BG*1.5, (0, 0))

    # Dibuja el barco, con o sin flip según corresponda
    if flip_horizontal:
        barco_flipped = pygame.transform.flip(barco, True, False)
        screen.blit(barco_flipped, barco_rect)
        def draw_triangle_with_barco(surface, color, pos, size):
            point1 = (barco_rect.left + 40, pos[1] + 20)
            point2 = (barco_rect.left + size + 40, pos[1] + size + 20)
            point3 = (barco_rect.left - size + 40, pos[1] + size + 20)
            pygame.draw.polygon(surface, color, [point1, point2, point3])
    else:
        screen.blit(barco, barco_rect)
        def draw_triangle_with_barco(surface, color, pos, size):
            point1 = (barco_rect.right - 40 , pos[1] + 20)
            point2 = (barco_rect.right - size - 40, pos[1] + size + 20)
            point3 = (barco_rect.right + size - 40, pos[1] + size + 20)
            pygame.draw.polygon(surface, color, [point1, point2, point3])

    # Dibuja el mar
    #pygame.draw.polygon(screen, constantes.MARCOLOR, constantes.MAR)

    # Mover y dibujar los círculos
    for circle in circles:
        circle[0] += circle[2]
        if circle[0] - 10 > constantes.ANCHURA_PANTALLA or circle[0] + 10 < 0:
            circle[2] *= -1
        imagen = pygame.image.load("basura.png")
        imagen = pygame.transform.scale(imagen, (imagen.get_width() * 2, imagen.get_height() * 2))
        screen.blit(imagen,(int(circle[0]), int(circle[1])))


    # Mover y dibujar los cuadrados
    for square in squares:

        square[0] += square[2]
        if square[0] + 15 > constantes.ANCHURA_PANTALLA or square[0] < 0:
            square[2] *= -1
        imagen2 = pygame.image.load("pez.png")
        imagen2 = pygame.transform.scale(imagen2, (imagen2.get_width() * 2, imagen2.get_height() * 2))
        screen.blit(imagen2,(square[0], square[1], 15, 15))

    # Dibujar el triángulo si está activo
    if triangle_active:
        draw_triangle_with_barco(screen, triangle_color, triangle_pos, triangle_size)

    # Mostrar el tiempo restante
    font = pygame.font.Font(None, 36)
    tiempo_texto = font.render(f"Tiempo: {tiempo_restante / 60:.0f}:{tiempo_restante % 60:.0f}", True, (0, 0, 0))
    screen.blit(tiempo_texto, (590, 10))

    # Mostrar la cantidad de cuadrados agarrados
    cuadrados_texto = font.render(f"Cuadrados: {cuadrados_agarrados}", True,  (0, 0, 0))
    screen.blit(cuadrados_texto, (590, 40))

    cuadrados_texto = font.render(f"Circulos: {circulos_agarrados}", True,  (0, 0, 0))
    screen.blit(cuadrados_texto, (590, 70))

    pygame.draw.rect(screen, constantes.BLACK, (10, 10, 90, 20), border_radius=20)
    if cuadrados_agarrados == pierdes:
        not pygame.draw.rect(screen, constantes.RED, (0, 0, 0, 0), border_radius=20)
    if cuadrados_agarrados < pierdes:
        pygame.draw.rect(screen, constantes.RED, (alt_x, 12, alt_y, 15), border_radius=20)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la tasa de frames
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
