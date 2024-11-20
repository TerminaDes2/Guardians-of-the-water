import pygame
import sys
import constantes
from barco import cargar_barco
from objetos import generar_circulos, generar_cuadrados
from objetos import objetos
from button import Button
#from botones_pausa import mostrar_pausa
#from menu_pausa import mostrar_pausa

screen = pygame.display.set_mode((constantes.ANCHURA_PANTALLA, constantes.ALTURA_PANTALLA))

# Definir las imágenes de los botones
btnsalida = pygame.image.load("img/saliro.png")
btnreiniciar = pygame.image.load("img/reiniciaro.png")
btnsiguiente = pygame.image.load("img/siguienteo.png")
btnsalida1 = pygame.image.load("img/saliro.png")
ganar = pygame.image.load("img/ganar.gif")

# Escalar las imágenes a un tamaño adecuado
btnsalida = pygame.transform.scale(btnsalida, (90, 90))
btnsalida1 = pygame.transform.scale(btnsalida, (90, 90))
btnreiniciar = pygame.transform.scale(btnreiniciar, (90, 90))
btnreiniciar1 = pygame.transform.scale(btnreiniciar, (90, 90))
btnsiguiente = pygame.transform.scale(btnsiguiente, (90, 90))

# Definir las posiciones de los botones
salida_position = (300, 300)
salida1_position = (600, 300)
reiniciar_position = (400, 300)
reiniciar1_position = (400, 300)
siguiente_position = (700, 500)

BGA = pygame.image.load("img/ganaro.png")
# Escalar la imagen al nuevo tamaño
BGA_escalado = pygame.transform.smoothscale(BGA, (800, 600))

BGP = pygame.image.load("img/perdiste.png")
# Escalar la imagen al nuevo tamaño
BGP_escalado = pygame.transform.smoothscale(BGP, (800, 600))

# Función para cambiar de música
def cambiar_musica(sound_gameplaying):
    pygame.mixer.music.load("img/musica2.wav")  # Cargar nueva canción
    pygame.mixer.music.play(-1)  # Reproducir en bucle
    pygame.mixer.music.set_volume(0.5)  # Establecer volumen   

# Funciones para cargar imágenes y escalarlas
def get_btns(size): 
    btns_image = pygame.image.load("img/sonidoo.png")
    return pygame.transform.scale(btns_image, size)

def get_btnns(size): 
    btnns_image = pygame.image.load("img/silecioo.png")
    return pygame.transform.scale(btnns_image, size)

# Variables del botón
buttonA_position = (400, 300)  # Posición
buttons_size = (90, 90)  # Tamaño
sound_off_image = get_btnns(buttons_size)  # Imagen de sonido desactivado
sound_on_image = get_btns(buttons_size)  # Imagen de sonido activado
buttonA_rect = pygame.Rect(buttonA_position, buttons_size)  # Rectángulo del botón
sound_playing = True  # Estado inicial del sonido

def toggle_sound():
    global sound_playing
    sound_playing = not sound_playing
    if sound_playing:
        pygame.mixer.music.unpause()  # Reanudar música
        print("Sonido activado")
    else:
        pygame.mixer.music.pause()  # Pausar música
        print("Sonido desactivado")

def siguiente_nivel():
    """Muestra los botones y devuelve la opción seleccionada"""
    while True:
        screen.blit(btnsiguiente, siguiente_position)  # Dibujar el botón de salida
    
        pygame.display.flip()  # Actualizar pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "nivel"  # Si se cierra el juego, salir

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnsiguiente.get_rect(topleft=siguiente_position).collidepoint(pygame.mouse.get_pos()):
                    return "nivel"  # Si se hace clic en "salir"

en_pausa = False  # Variable global para manejar el estado de pausa

def mostrar_pausas():
    """Muestra el botón de salida durante la pausa."""
    global en_pausa
    en_pausa = True  # Activar el estado de pausa
    while en_pausa:
        screen.blit(btnsalida1, salida1_position)  # Dibujar el botón de salida
        pygame.display.flip()  # Actualizar la pantalla para mostrar los cambios

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Cerrar el juego completamente

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnsalida1.get_rect(topleft=salida1_position).collidepoint(pygame.mouse.get_pos()):
                    en_pausa = False  # Desactivar pausa
                    return "volver"  # Regresar al menú principal

def mostrar_botones():
    """Muestra los botones y devuelve la opción seleccionada."""
    while not en_pausa:  # Solo mostrar los botones si no está en pausa
        screen.blit(btnreiniciar, reiniciar_position)  # Dibujar el botón de reiniciar
        screen.blit(btnsalida, salida_position)  # Dibujar el botón de salida

        pygame.display.flip()  # Actualizar pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "salir"  # Si se cierra el juego, salir

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnreiniciar.get_rect(topleft=reiniciar_position).collidepoint(pygame.mouse.get_pos()):
                    return "reiniciar"  # Si se hace clic en "reiniciar"
                elif btnsalida.get_rect(topleft=salida_position).collidepoint(pygame.mouse.get_pos()):
                    return "volver"  # Si se hace clic en "salir"

def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("img/Bakery.ttf", size)

BGC = pygame.image.load("img/controles.jpg")
nuevo_tamaño = (800, 600)  # Cambia estos valores al tamaño deseado
# Escalar la imagen al nuevo tamaño
BGC_escalado = pygame.transform.scale(BGC, nuevo_tamaño)

#sa
def juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv):
    pygame.init()
    #cambiar_musica("img/musica2.wav")
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    screen = pygame.display.set_mode((constantes.ANCHURA_PANTALLA, constantes.ALTURA_PANTALLA))
    pygame.display.set_caption("Guardians the Ocean")

    icon = pygame.image.load("img/LogoG.png")
    icon = pygame.transform.scale(icon, (icon.get_width() * 10, icon.get_height() * 10))
    pygame.display.set_icon(icon)

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("img/Bakery.ttf", size)
    
    # Crear instancia del botón
    btnsalida = Button(
        image=btnsalida1,
        pos=(450, 350),  # Posición del botón
        text_input="",   # Si no tiene texto, se deja vacío
        font=get_font(35),       # Si no usas fuente, pon None
        base_color="#d7fcd4", # Color base, si aplica
        hovering_color="white" # Color al hacer hover, si aplica
    )

    def render_text(text, size, color, position, surface):
        font = get_font(size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        surface.blit(text_surface, text_rect)

    # Cargar imágenes del botón de pausa y reanudar
    pause_image = pygame.image.load("img/playo.png")
    resume_image = pygame.image.load("img/renaudaro.png")
    control_image = pygame.image.load("img/controlo.png")

    # Escalar las imágenes a un tamaño adecuado para el botón
    pause_image = pygame.transform.scale(pause_image, (90, 90))
    resume_image = pygame.transform.scale(resume_image, (90, 90))
    control_image = pygame.transform.scale(control_image, (90, 90))

    pause_position=(685,20)
    resume_position=(685,20)

    # Inicializar el rectángulo del botón de pausa
    button_rect = pygame.Rect(695, 29, 90, 90)
    button_rect2 = pygame.Rect(695, 29, 90, 90)
    button_rect3 = pygame.Rect(300, 300, 90, 90)
    button_rect4 = pygame.Rect(200, 300, 90, 90)
    button_rect5 = pygame.Rect(500, 300, 90, 90) #reiniciar pausa

    def draw_button(screen, paused):
        global sound_playing, current_screen  # Asegúrate de usar la variable global para alternar el estado del soni
        mouse_pos = pygame.mouse.get_pos()  # Obtener posición del mouse
        if paused:

            # Dibujar imágenes de botones
            screen.blit(resume_image, button_rect2.topleft)
            screen.blit(btnreiniciar1, button_rect3.topleft)
            screen.blit(btnsalida1, button_rect4.topleft)
            screen.blit(control_image, button_rect5.topleft)
            
                # Mostrar el botón de sonido según su estado
            if sound_playing:
                screen.blit(sound_on_image, buttonA_position)
            else:
                screen.blit(sound_off_image, buttonA_position)

            # Dibuja un rectángulo para depuración
            #pygame.draw.rect(screen, (255, 0, 0), buttonA_rect, 2)

            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Clic detectado en posición: {mouse_pos}")
                    print(f"Rectángulo del botón: {buttonA_rect}")
                    if buttonA_rect.collidepoint(mouse_pos):
                        print("Botón de sonido clicado")
                        toggle_sound()
                    if button_rect5.collidepoint(mouse_pos):
                        controls(screen)
                                  
        else:
            screen.blit(pause_image, button_rect.topleft)  # Mostrar imagen de "pausa"

        # Aplicar hover y dibujar el botón
            #button_rect4.collidepoint(mouse_pos)  # Detecta hover
            #btnsalida.hoverEffect(mouse_pos)  # Detecta hover

            #if pygame.mouse.get_pressed():  # Verifica si el botón izquierdo del ratón ha sido presionado
                #btnsalida.update(screen)  # Dibuja el botón con el efecto de hover
                #print("Se hizo clic en 'Volver'")  # Depuración: Verifica si el clic se registró
                #return "volver"  # Retorna "volver" cuando se hace clic en el botón

    def controls(screen):
     global p
     global current_screen
     while True:
        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.fill("white")
        screen.blit(BGC_escalado, (0, 0))

       # CONTROLS_TEXT = get_font(90).render(textos[idioma_actual]["controls"], True, "Black")
        #CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=(400, 100))
        #SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        CONTROLS_BACK = Button(image=None, pos=(100, 550), 
                            text_input="<-", font=get_font(50), base_color="Black", hovering_color="blue")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                 return

        pygame.display.update()

    # Cargar el barco
    barco, barco_rect = cargar_barco()

    def gestor_niv(niv, idioma_actual, advanced):
        global circulos, cuadrados, tiempo_limite, pierdes

        if niv == 1:
            circulos = 10
            cuadrados = 10
            tiempo_limite = 300
            pierdes = 7
            sp1 = 0
            sp2 = 1
            sp3 = 2
            sp4 = 3
            objetos(sp1, sp2, sp3, sp4)
            juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv)
        if niv == 2:
            circulos = 10
            cuadrados = 10
            tiempo_limite = 200
            pierdes = 5
            sp1 = 1
            sp2 = 2
            sp3 = 3
            sp4 = 4
            objetos(sp1, sp2, sp3, sp4)
            juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv)
        if niv == 3:
            circulos = 10
            cuadrados = 10
            tiempo_limite = 120
            pierdes = 3
            sp1 = 2
            sp2 = 3
            sp3 = 4
            sp4 = 5
            objetos(sp1, sp2, sp3, sp4)
            juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv)
        if niv > 3:
            #print("Felicidades, completaste el juego")
            return "volver"
        
    # Recibe los valores del main.py
    print(circulos)
    print(cuadrados)
    print(tiempo_limite) 
    print(pierdes)
    print(idioma_actual)
    print(advanced)
    print(idioma_actual)
    print(niv)

    textos = {
        "en": {
            "keep": "Keep trying",
            "win": "You Win",
            "time": "Time",
            "squares": "Fishes",
            "circles": "Trash",
            "lost": "Try again",
            "pause": "Pause",
        },
        "es": {
        "keep": "Sigue intentando",
            "win": "Felicidades, ganaste",
            "time": "Tiempo",
            "squares": "Peces",
            "circles": "Basura",
            "lost": "Sigue intentando",
            "pause": "Pausa",
        }
    }

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
    triangle_pos = [constantes.ANCHURA_PANTALLA // 2, 110]
    triangle_size = 20

    if advanced == 1:
        triangle_velocidad = 450
    else:
        triangle_velocidad = 800

    triangle_active = True
    triangle_movement = False
    triangle_direction = 1
    triangle_timer = 0
    collision_detected = False
    colisiones_activas = True

    #Cantidad de animales que puedes agarrar para perder
    #pierdes = 5

    # Variables del contador
    start_ticks = pygame.time.get_ticks()  # Tiempo inicial
    cuadrados_agarrados = 0  # Contador de cuadrados agarrados
    circulos_agarrados = 0  # Contador de circulos agarrados
    #tiempo_limite = 120  # Minutos en segundos

    # Generar círculos y cuadrados
    circles = generar_circulos(circulos, 10)
    squares = generar_cuadrados(cuadrados, 15)

    #copia la cantidad de elementos en la lista circles
    circulos_eliminables = len(circles)

    def dibujar_soga(surface, inicio, fin):
        # Dibuja una línea (soga) entre la posición de inicio (altura máxima) y la posición de fin (altura actual)
        pygame.draw.line(surface, (132, 89, 14), inicio, fin, 5)  # Color blanco y grosor 5

    # Función para verificar colisiones
    def check_collision(triangle_pos, triangle_size, obj_pos, obj_size):
        if flip_horizontal:
            triangle_rect = pygame.Rect(barco_rect.left - triangle_size + 45, triangle_pos[1] + 20, triangle_size , triangle_size)
            #print(triangle_rect)
        else:  
            triangle_rect = pygame.Rect(barco_rect.right - triangle_size - 25, triangle_pos[1] + 20, triangle_size , triangle_size)
            #print(triangle_rect)

        obj_rect = pygame.Rect(obj_pos[0], obj_pos[1], obj_size, obj_size)
        #pygame.draw.rect(screen, (255, 255, 0), obj_rect, 2)
        #pygame.draw.rect(screen, (0, 255, 0), triangle_rect, 2)
        return triangle_rect.colliderect(obj_rect)

    # Cargar la imagen de fondo y escalarla
    if niv == 1:
        fondo = pygame.image.load("img/fondo_dia.png")
    if niv == 2:
        fondo = pygame.image.load("fondo22.png")
    if niv == 3:
        fondo = pygame.image.load("img/fondo_noche.png")
    
    fondo_escalado = pygame.transform.scale(fondo, (800, 600))

    # Variables de tiempo
    start_ticks = pygame.time.get_ticks()
    paused_time = 0
    paused_ticks = 0

    # Bucle principal
    clock = pygame.time.Clock()
    paused = False
    running = True
    sound_was_playing_before_pause = True  # Nuevo estado para recordar si el sonido estaba activo antes de la pausa
   
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Obtener las teclas presionadas
            keys = pygame.key.get_pressed()

            # Detectar clic del ratón o boton escape
            if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_ESCAPE]:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos) or keys[pygame.K_ESCAPE]:
                    paused = not paused  # Cambiar el estado de pausa
                    if paused:
                        paused_ticks = pygame.time.get_ticks()  # Marca el tiempo al momento de pausar
                    else:
                        # Acumula el tiempo de pausa al reanudar
                        paused_time += pygame.time.get_ticks() - paused_ticks
                        
                if button_rect3.collidepoint(mouse_pos) and paused:
                    return "reiniciar"
                if button_rect4.collidepoint(mouse_pos) and paused:
                    return "volver"

        # Dibuja el fondo y botón de pausa
        screen.blit(fondo_escalado, (0, 0))
        draw_button(screen, paused)

        if paused:
            font_size = 80
            texto_pausa = get_font(font_size).render(textos[idioma_actual]["pause"], True, (255, 255, 255))
            screen.blit(texto_pausa, (constantes.ANCHURA_PANTALLA // 2 - 100, constantes.ALTURA_PANTALLA // 2 - 100))
            pygame.display.flip() 
            continue

        # Calcula el tiempo restante ajustado
        segundos_transcurridos = (pygame.time.get_ticks() - start_ticks - paused_time) / 1000
        tiempo_restante = tiempo_limite - segundos_transcurridos
                
        # Verificar si el tiempo se agotó
        if tiempo_restante <= 0 or cuadrados_agarrados >= pierdes :
            # Mostrar mensaje de "Perdiste"
            screen.fill("black")
            screen.blit(BGP_escalado, (0, 0))
            font_size = 60
            
            texto_perdiste = get_font(font_size).render(textos[idioma_actual]["lost"], True, (255, 255, 255))
            screen.blit(texto_perdiste, (constantes.ANCHURA_PANTALLA // 2 - 250, constantes.ALTURA_PANTALLA // 2 - 100))

            pygame.display.flip()  # Actualizar la pantalla para mostrar el mensaje de "Perdiste"

            opcion = mostrar_botones()  # Mostrar los botones de "Reiniciar" y "Salir"

            if opcion == "volver":
                return "volver"  # Regresa al menú
            elif opcion == "reiniciar":
                return "reiniciar"  # Reinicia el nivel
        
        hover = pygame.mixer.Sound("img/win.mp3")
        
        if circulos_agarrados == circulos_eliminables:
            pygame.mixer.music.pause()  # Pause the music
            hover.play()
            font = pygame.font.Font(None, 74)
            screen.fill("black")
            screen.blit(BGA_escalado, (0, 0))
            font_size=60
            texto_ganaste = get_font(font_size).render(textos[idioma_actual]["win"], True, (255, 255, 255))
            screen.blit(texto_ganaste, (constantes.ANCHURA_PANTALLA // 2 - 250, constantes.ALTURA_PANTALLA // 2 - 100))
            pygame.display.flip()
            prueb = siguiente_nivel()
            niv += 1
            if prueb == "nivel":
                pygame.mixer.music.unpause()
                return "sig"
            
            #return "volver"
            # Resume the music

        keys = pygame.key.get_pressed()
        # Mover el barco y ajustar la dirección
        if keys[pygame.K_a] and triangle_movement == False and barco_rect.left > -24 or keys[pygame.K_LEFT] and triangle_movement == False and barco_rect.left > -24:
            barco_rect.x -= velocidad
            flip_horizontal = True
        if keys[pygame.K_d] and triangle_movement == False and barco_rect.right < constantes.ANCHURA_PANTALLA + 24 or keys[pygame.K_RIGHT] and triangle_movement == False and barco_rect.right < constantes.ANCHURA_PANTALLA + 24:
            barco_rect.x += velocidad
            flip_horizontal = False

        # Activar el triángulo cuando se presiona la barra espaciadora
        if keys[pygame.K_SPACE] and triangle_movement == False or keys[pygame.K_DOWN] and triangle_movement == False or keys[pygame.K_s] and triangle_movement == False:
            triangle_movement = True
            triangle_direction = 1  # El triángulo comienza a bajar
            triangle_timer = pygame.time.get_ticks()
            triangle_pos[1] = 110  # Posición inicial del triángulo
            collision_detected = False
            movimiento_permitido = False
            velocidad = 0
            if advanced == 1:
                triangle_velocidad = 450
            else:
                triangle_velocidad = 800

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
                        if advanced == 1:
                            triangle_velocidad = 200
                elif triangle_direction == -1:  # Subiendo
                    triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000
                    if triangle_pos[1] <= 110:
                        triangle_movement = False
                        velocidad = 0
                        triangle_movement = False  # Termina el ciclo
                        triangle_pos[1] = 110
                        movimiento_permitido = True
                        velocidad = 5
                        colisiones_activas = True  # Activar colisiones al llegar a su altura original

            if collision_detected:  # Si se detecta una colisión
                colisiones_activas = False  # Desactivar colisiones al colisionar con un objeto
                triangle_direction = -1  # Asegúra de que siempre suba tras colisión
                triangle_pos[1] -= triangle_velocidad * clock.get_time() / 1000  # Subir
                if triangle_pos[1] <= 110:  # Si ya ha subido completamente
                    triangle_pos[1] = 110
                    movimiento_permitido = True
                    velocidad = 5
                    triangle_movement = False  # Detener el triángulo
                    collision_detected = False  # Resetear la colisión para futuros movimientos
                    colisiones_activas = True  # Activar colisiones al colisionar con un objeto

            if colisiones_activas:
                for circle in circles:
                    #circle_rect = pygame.Rect(circle[0]+15, circle[1]+15, 20, 20)  # Rectángulo del círculo
                    #pygame.draw.rect(screen, (0, 0, 255), circle_rect, 2)  # Azul para círculos
                    if check_collision(triangle_pos, triangle_size, (circle[0]+15, circle[1]+15), 10 * 2):
                        collision_detected = True
                        colisiones_activas = False  # Desactivar colisiones
                        triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir
                        circles.remove(circle) #Elimina el circulo golpeado
                        circulos_agarrados += 1  # Aumentar contador de circulos agarrados                     
 
                for square in squares:
                    #square_rect = pygame.Rect(square[0], square[1], 15, 15)  # Rectángulo del cuadrado
                    #pygame.draw.rect(screen, (255, 0, 255), square_rect, 2)  # Magenta para cuadrados
                    if check_collision(triangle_pos, triangle_size, (square[0], square[1]), 15):
                        collision_detected = True
                        colisiones_activas = False  # Desactivar colisiones
                        if advanced == 1:
                            triangle_velocidad = 200
                        triangle_direction = -1  # Si hay colisión, el triángulo comienza a subir
                        squares.remove(square) #Elimina el cuadrado golpeado
                        cuadrados_agarrados += 1  # Aumentar contador de cuadrados agarrados
                        
                        #Calcula la barra de vida
                        alt_x += (divisible / (pierdes - 1))*2
                        alt_y -= (divisible / (pierdes - 1))*2

        # Dibuja el fondo
        #screen.fill(constantes.CIELO)
        #pygame.draw.polygon(screen, constantes.MARCOLOR, constantes.MAR)
        #screen.blit(BG*1.5, (0, 0))

        # Dibuja el barco, con o sin flip según corresponda
        if flip_horizontal:
            barco_flipped = pygame.transform.flip(barco, True, False)
            screen.blit(barco_flipped, barco_rect)
            triangle_pos[0] = barco_rect.left + 5
            def draw_mastil(surface, color, pos, size):
                point1 = (barco_rect.left + 40, pos[1] + 20)
                point2 = (barco_rect.left + size + 40, pos[1] + size + 20)
                #6pygame.draw.polygon(surface, color, [point1, point2])
                
        else:
            screen.blit(barco, barco_rect)
            triangle_pos[0] = barco_rect.left + 135
            def draw_mastil(surface, color, pos, size):
                point1 = (barco_rect.right - 40 , pos[1] + 20)
                point2 = (barco_rect.right - size - 40, pos[1] + size + 20)
                #pygame.draw.polygon(surface, color, [point1, point2])
                
        # Dibuja el mar
        #pygame.draw.polygon(screen, constantes.MARCOLOR, constantes.MAR)

        # Mover y dibujar los círculos
        for circle in circles:
            circle[0] += circle[2]
            if circle[0] > constantes.ANCHURA_PANTALLA - 30 or circle[0] + 10 < 0:
                circle[2] *= -1
            imagen = pygame.image.load("basura.png")
            imagen = pygame.transform.scale(imagen, (imagen.get_width() * 2, imagen.get_height() * 2))
            screen.blit(imagen,(int(circle[0]), int(circle[1])))

        # Mover y dibujar los cuadrados
        for square in squares:
            imagen2 = pygame.image.load("img/pez_glo.png")
            imagen2 = pygame.transform.scale(imagen2, (imagen2.get_width(), imagen2.get_height()))
            square[0] += square[2]
            if square[0] + 15 > constantes.ANCHURA_PANTALLA or square[0] < 0:
                square[2] *= -1
                square[3] *= -1  # Invertir la dirección para el flip
            #imagen2 = pygame.image.load("pez.png")
            #imagen2 = pygame.transform.scale(imagen2, (imagen2.get_width() * 2, imagen2.get_height() * 2))
            if square[3] == 1:
                cuadrado_flipped = pygame.transform.flip(imagen2, True, False)
                screen.blit(cuadrado_flipped, (square[0]-5, square[1], 15, 15))
            else:
                screen.blit(imagen2, (square[0]-15, square[1], 15, 15))

        inicio_soga = (triangle_pos[0] + 30, 115)  # Posición inicial (altura máxima)
        fin_soga = (triangle_pos[0] + 30, triangle_pos[1] + 5)  # Posición actual (donde está el triángulo)
        dibujar_soga(screen, inicio_soga, fin_soga)

        # Dibujar el triángulo si está activo
        garra = pygame.image.load("img/garra1.png")
        garra = pygame.transform.scale(garra, (garra.get_width() * 2, garra.get_height() * 2))
        if triangle_active:
            draw_mastil(screen, triangle_color, triangle_pos, triangle_size)
            screen.blit(garra,(int(triangle_pos[0] + 10), int(triangle_pos[1])))

        # Mostrar el tiempo restante
        pygame.draw.rect(screen, constantes.BLACK, (510, 45, 170, 37), border_radius=20)
        pygame.draw.rect(screen, constantes.WHITE, (510, 47, 170, 32), border_radius=20)
        font = pygame.font.Font(None, 50)
        font_size=40
        minutos = int(tiempo_restante // 60)
        segundos = int(tiempo_restante % 60)

        # Formatear los minutos y segundos para que siempre tengan dos dígitos
        minutos_formateados = f"{minutos:02d}"
        segundos_formateados = f"{segundos:02d}"

        tiempo_texto = font.render(f'{minutos_formateados}:{segundos_formateados}', True, (0, 0, 0))
        screen.blit(tiempo_texto, (555, 47))

        # Mostrar la cantidad de cuadrados agarrados
        #cuadrados_texto = font.render(f"Cuadrados: {cuadrados_agarrados}", True,  (0, 0, 0))
        #screen.blit(cuadrados_texto, (590, 40))
        font = pygame.font.Font(None, 40)
        font_size = 30
        cuadrados_texto = get_font(font_size).render(f"{circulos_agarrados} / 10", True,  (0, 0, 0))
        screen.blit(cuadrados_texto, (360, 70))

        pygame.draw.rect(screen, constantes.BLACK, (110, 45, 170, 35), border_radius=20)
        if cuadrados_agarrados == pierdes:
            not pygame.draw.rect(screen, constantes.RED, (0, 0, 0, 0), border_radius=20)
        if cuadrados_agarrados < pierdes:
            pygame.draw.rect(screen, constantes.RED, (alt_x + 110 - 10, 47,  alt_y + 80, 30), border_radius=20)
        
        # Cargar imágenes 
            peztriste_image = pygame.image.load("img/c.png")
            reloj_image = pygame.image.load("img/RELOJ.png")
            basura_image = pygame.image.load("img/basura.png")

            # Escalar las imágenes a un tamaño adecuado para el botón
            peztriste_image = pygame.transform.scale(peztriste_image, (100, 80))
            reloj_image = pygame.transform.scale(reloj_image, (60, 60))
            basura_image = pygame.transform.scale(basura_image, (60, 60))

            peztriste_pos = (55, 20)  # Posición del pez triste
            reloj_pos = (475, 29)      # Posición del reloj
            basura_pos = (360, 15)

            # Mostrar las imágenes en la pantalla
            screen.blit(peztriste_image, peztriste_pos)
            screen.blit(reloj_image, reloj_pos)
            screen.blit(basura_image, basura_pos)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la tasa de frames
        clock.tick(60)

    # Cerrar Pygame
    pygame.quit()
    sys.exit()


