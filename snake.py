import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)  # Color de fondo azul

# Tamaño de la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Snake")

# Tamaño de la serpiente y velocidad
TILE_SIZE = 20
initial_fps = 5  # Velocidad inicial de la serpiente
fps_increase = 1  # Aumento de velocidad por fruta
FPS = initial_fps

# Inicialización de la serpiente
snake = [(100, 100), (80, 100), (60, 100)]
direction = (TILE_SIZE, 0)

# Lista de imágenes de frutas
fruit_images = ["apple.png", "hola.png", "images.png"]  # Añadir más nombres de archivos según las imágenes disponibles
loaded_fruits = [pygame.transform.scale(pygame.image.load(img), (TILE_SIZE, TILE_SIZE)) for img in fruit_images]

# Inicialización de la primera fruta aleatoria
current_fruit_image = random.choice(loaded_fruits)
apple = (random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
         random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE)

# Función para dibujar la serpiente
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, TILE_SIZE, TILE_SIZE))

# Función para dibujar la fruta
def draw_fruit(apple, fruit_image):
    screen.blit(fruit_image, apple)

# Función para mover la serpiente
def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)
    snake.pop()

# Función para verificar colisiones
def check_collisions(snake):
    head = snake[0]
    # Colisión con los bordes
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Colisión con sí misma
    if head in snake[1:]:
        return True
    return False

# Función para generar nueva fruta aleatoria
def spawn_fruit(snake):
    while True:
        fruit = (random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
                 random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE)
        if fruit not in snake:
            return fruit

# Función para mostrar el menú de inicio
def show_start_menu():
    font = pygame.font.Font(None, 36)
    text = font.render("Presiona cualquier tecla para empezar", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(RED)
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Espera a que el jugador presione una tecla
waiting = True
while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Bucle principal del juego
def main_game_loop():
    global FPS, apple, current_fruit_image, direction, snake
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, TILE_SIZE):
                    direction = (0, -TILE_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -TILE_SIZE):
                    direction = (0, TILE_SIZE)
                elif event.key == pygame.K_LEFT and direction != (TILE_SIZE, 0):
                    direction = (-TILE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-TILE_SIZE, 0):
                    direction = (TILE_SIZE, 0)

        # Mover la serpiente
        move_snake(snake, direction)

        # Comprobar si la serpiente ha comido la fruta
        if snake[0] == apple:
            snake.append(snake[-1])  # Crece la serpiente
            apple = spawn_fruit(snake)  # Nueva fruta
            current_fruit_image = random.choice(loaded_fruits)  # Seleccionar nueva imagen de fruta aleatoria
            FPS += fps_increase  # Aumenta la velocidad

        # Comprobar colisiones
        if check_collisions(snake):
            running = False

        # Dibujar todo en la pantalla
        screen.fill(BLUE)  # Cambia el color de fondo a azul
        draw_snake(snake)
        draw_fruit(apple, current_fruit_image)  # Dibuja la fruta actual
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(FPS)

# Mostrar el menú de inicio antes de comenzar el juego
show_start_menu()
main_game_loop()
pygame.quit()
