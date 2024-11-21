import pygame
import sys
import cv2
from button import Button

idioma_actual = "es"

textos = {
    "en": {
        "play": "Play",
        "levels": "Levels",
        "settings": "Settings",
        "language": "Language",
        "controls": "Controls",
        "back": "< Back",
        "level1": "Level 1",
        "level2": "Level 2",
        "level3": "Level 3",
        "begginer": "Beginner",
        "advanced": "Advanced",
        "about": "About Us",
        "sound": "Sound",
        "nosound": "No Sound",
        "pause": "Pause",
        "quit": "Quit",
        "instrucciones": "img/instruesp1",
    },
    "es": {
        "play": "Jugar",
        "levels": "Niveles",
        "settings": "Configuración",
        "language": "Idioma",
        "controls": "Controles",
        "back": "< Atrás",
        "level1": "Nivel 1",
        "level2": "Nivel 2",
        "level3": "Nivel 3",
        "begginer": "Principiante",
        "advanced": "Avanzado",
        "about": "Nosotros",
        "sound": "Sonido",
        "nosound": "Sin Sonido",
        "pause": "Pausa",
        "quit": "Salir",
        "instrucciones": "img/instruingle1",
    }
}

SCREEN = pygame.display.set_mode((800, 600))

BG = pygame.image.load("img/fondo.jpg")
nuevo_tamaño = (800, 600)  # Cambia estos valores al tamaño deseado
# Escalar la imagen al nuevo tamaño
BG_escalado = pygame.transform.scale(BG, nuevo_tamaño)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/Bakery.ttf", size)

def reproducir_video_ingles():
    # Inicializar Pygame y OpenCV
    pygame.mixer.init()

    # Cargar el video
    cap = cv2.VideoCapture('img/creditos_ingles.mp4')
    if not cap.isOpened():
        print("Error al abrir el video")
        sys.exit()

    clock = pygame.time.Clock()
    running = True

    OPTIONS_BACK = Button(
            image=None, 
            pos=(100, 550), 
            text_input=textos[idioma_actual]["back"], 
            font=get_font(50), 
            base_color="Black", 
            hovering_color="blue"
        )
   
    while running:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    cap.release()
                    return
                    


        # Leer el siguiente frame del video
        ret, frame = cap.read()
        if not ret:
            cap.release()
        
            return
        
         # Leer el siguiente frame del video
        ret, frame = cap.read()
        if not ret:
            cap.release()
            return
        

        # Rotar el video 90 grados a la derecha
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame = cv2.flip(frame, 0)

        # Redimensionar y centrar el video
        video_width, video_height = 360, 640  # Cambiar las dimensiones después de rotar
        frame = cv2.resize(frame, (video_width, video_height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame)
        video_x = (800 - video_height) // 2
        video_y = (600 - video_width) // 2
        # Dibujar el fondo y el video centrado
        SCREEN.blit(BG_escalado, (0, 0))
        SCREEN.blit(frame_surface, (video_x, video_y))
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Actualizar la pantalla
        pygame.display.update()
        clock.tick(30)




