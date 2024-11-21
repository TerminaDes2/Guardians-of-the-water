import pygame
import sys
import cv2




def reproducir_video():
    pygame.init()
    pygame.mixer.init()

    # Configuración de la pantalla
    window_width, window_height = 800, 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Video en Pantalla Completa')


    # Cargar el video usando OpenCV
    cap = cv2.VideoCapture('img/creditos_español.mp4')

    if not cap.isOpened():
        print("Error al abrir el video")
        sys.exit()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Leer frame por frame del video
        ret, frame = cap.read()
        if not ret:
            return 

        # Rotar el frame 90 grados en sentido antihorario si es necesario
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Voltear horizontalmente para reflejo en espejo
        frame = cv2.flip(frame, 0)

        # Redimensionar el frame para que ocupe toda la pantalla
        frame = cv2.resize(frame, (400, 300))

        # Convertir el frame de BGR (OpenCV) a RGB (Pygame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertir a superficie de Pygame
        frame_surface = pygame.surfarray.make_surface(frame)

        # Dibujar el frame en la pantalla
        screen.blit(frame_surface, (0, -100))  # Coordenadas (0, 0) para ocupar toda la pantalla

        # Actualizar la pantalla
        pygame.display.update()
        clock.tick(30)

    cap.release()
    pygame.quit()



