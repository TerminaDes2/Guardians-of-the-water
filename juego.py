import pygame
import sys
import constantes
from barco import cargar_barco
from objetos import generar_circulos, generar_cuadrados
from objetos import objetos

#sa
def juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv):
    pygame.init()

    screen = pygame.display.set_mode((constantes.ANCHURA_PANTALLA, constantes.ALTURA_PANTALLA))
    pygame.display.set_caption("Guardians of the Ocean")

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("img/Bakery.ttf", size)

    def render_text(text, size, color, position, surface):
        font = get_font(size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        surface.blit(text_surface, text_rect)

    # Cargar imágenes del botón de pausa y reanudar
    pause_image = pygame.image.load("img/pausa.png")
    resume_image = pygame.image.load("img/play.png")

    # Escalar las imágenes a un tamaño adecuado para el botón
    pause_image = pygame.transform.scale(pause_image, (90, 90))
    resume_image = pygame.transform.scale(resume_image, (70, 70))


    # Inicializar el rectángulo del botón de pausa
    button_rect = pygame.Rect(685, 20, 100, 50)
    button_rect2 = pygame.Rect(695, 29, 100, 50)

    # Dibujar el botón basado en el estado de pausa
    def draw_button(screen, paused):
        if paused:
            screen.blit(resume_image, button_rect2.topleft)  # Mostrar imagen de "reanudar"
        else:
            screen.blit(pause_image, button_rect.topleft)  # Mostrar imagen de "pausa"

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
            print("Felicidades, completaste el juego")


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
    triangle_pos = [constantes.ANCHURA_PANTALLA // 2, 100]
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

    # Función para verificar colisiones
    def check_collision(triangle_pos, triangle_size, obj_pos, obj_size):
        if flip_horizontal:
            triangle_rect = pygame.Rect(barco_rect.left - triangle_size + 40, triangle_pos[1] + 20, triangle_size * 2, triangle_size)
            #print(triangle_rect)
        else:  
            triangle_rect = pygame.Rect(barco_rect.right - triangle_size - 40, triangle_pos[1] + 20, triangle_size * 2, triangle_size)
            #print(triangle_rect)

        obj_rect = pygame.Rect(obj_pos[0], obj_pos[1], obj_size, obj_size)
        return triangle_rect.colliderect(obj_rect)

    # Cargar la imagen de fondo y escalarla
    fondo = pygame.image.load("fondo22.png")
    fondo_escalado = pygame.transform.scale(fondo, (800, 600))

    # Variables de tiempo
    start_ticks = pygame.time.get_ticks()
    paused_time = 0
    paused_ticks = 0

    # Bucle principal
    clock = pygame.time.Clock()
    paused = False
    running = True
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

        # Dibuja el fondo y botón de pausa
        screen.blit(fondo_escalado, (0, 0))
        draw_button(screen, paused)

        if paused:
            font_size = 80
            texto_pausa = get_font(font_size).render(textos[idioma_actual]["pause"], True, (255, 255, 255))
            screen.blit(texto_pausa, (constantes.ANCHURA_PANTALLA // 2 - 100, constantes.ALTURA_PANTALLA // 2 - 50))
            pygame.display.flip()
            continue

        # Calcula el tiempo restante ajustado
        segundos_transcurridos = (pygame.time.get_ticks() - start_ticks - paused_time) / 1000
        tiempo_restante = tiempo_limite - segundos_transcurridos

        # Verificar si el tiempo se agotó
        if tiempo_restante <= 0 or cuadrados_agarrados >= pierdes :
            # Mostrar mensaje de "Perdiste"
            screen.fill("black")
            font_size = 60
            
            texto_perdiste= get_font(font_size).render(textos[idioma_actual]["lost"], True, (255, 255, 255))
            screen.blit(texto_perdiste, (constantes.ANCHURA_PANTALLA // 2 - 250, constantes.ALTURA_PANTALLA // 2 - 100))
            pygame.display.flip()
            pygame.time.wait(3000)
            gestor_niv(niv, idioma_actual, advanced)
            #running = False
            
        if circulos_agarrados == circulos_eliminables:
            font = pygame.font.Font(None, 74)
            font_size=60
            texto_ganaste = get_font(font_size).render(textos[idioma_actual]["win"], True, (255, 255, 255))
            screen.blit(texto_ganaste, (constantes.ANCHURA_PANTALLA // 2 - 70, constantes.ALTURA_PANTALLA // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            niv += 1
            gestor_niv(niv, idioma_actual, advanced)
            #running = False

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
            triangle_pos[0] = barco_rect.left
            def draw_mastil(surface, color, pos, size):
                point1 = (barco_rect.left + 40, pos[1] + 20)
                point2 = (barco_rect.left + size + 40, pos[1] + size + 20)
                #6pygame.draw.polygon(surface, color, [point1, point2])
                
        else:
            screen.blit(barco, barco_rect)
            triangle_pos[0] = barco_rect.left + 130
            def draw_mastil(surface, color, pos, size):
                point1 = (barco_rect.right - 40 , pos[1] + 20)
                point2 = (barco_rect.right - size - 40, pos[1] + size + 20)
                #pygame.draw.polygon(surface, color, [point1, point2])
                

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
            imagen2 = pygame.image.load("pez.png")
            imagen2 = pygame.transform.scale(imagen2, (imagen2.get_width() * 2, imagen2.get_height() * 2))
            square[0] += square[2]
            if square[0] + 15 > constantes.ANCHURA_PANTALLA or square[0] < 0:
                square[2] *= -1
                square[3] *= -1  # Invertir la dirección para el flip
            imagen2 = pygame.image.load("pez.png")
            imagen2 = pygame.transform.scale(imagen2, (imagen2.get_width() * 2, imagen2.get_height() * 2))
            if square[3] == 1:
                cuadrado_flipped = pygame.transform.flip(imagen2, True, False)
                screen.blit(cuadrado_flipped, (square[0], square[1], 15, 15))
            else:
                screen.blit(imagen2, (square[0], square[1], 15, 15))

        # Dibujar el triángulo si está activo
        garra = pygame.image.load("img/garra.png")
        garra = pygame.transform.scale(garra, (garra.get_width() * 0.5, garra.get_height() * 0.5))
        if triangle_active:
            draw_mastil(screen, triangle_color, triangle_pos, triangle_size)
            screen.blit(garra,(int(triangle_pos[0]), int(triangle_pos[1])))

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
            peztriste_image = pygame.image.load("img/PEZTRISTE.png")
            reloj_image = pygame.image.load("img/RELOJ.png")
            basura_image = pygame.image.load("img/basura.png")

            # Escalar las imágenes a un tamaño adecuado para el botón
            peztriste_image = pygame.transform.scale(peztriste_image, (100, 100))
            reloj_image = pygame.transform.scale(reloj_image, (60, 60))
            basura_image = pygame.transform.scale(basura_image, (60, 60))

            peztriste_pos = (55, 10)  # Posición del pez triste
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
