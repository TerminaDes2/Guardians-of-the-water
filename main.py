import json
import subprocess
import pygame, sys
from button import Button
from juego import juego
from objetos import objetos
from juego import mostrar_botones, siguiente_nivel
from botones_pausa import mostrar_pausa


pygame.init()

idioma_actual = "es"
advanced = 0
# Diccionario con configuraciones de los niveles
niveles_config = {
    "BEGGINER": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 300,  # 5 minutos
        "pierdes": 7,
        "idioma": idioma_actual,
        "v1": 0,
        "v1,1": 1,
        "v2": 1,
        "v2,1": 2,
        "v3": 2,
        "v3,1": 3,
        "advanced": advanced,
        "niv":1
    },
    "INTERMEDIATE": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 200,  # 3 minutos y 20 segundos
        "pierdes": 5,
        "idioma": idioma_actual,
        "v1": 1,
        "v1,1": 2,
        "v2": 2,
        "v2,1": 3,
        "v3": 3,
        "v3,1": 4,
        "advanced": advanced,
        "niv":2
    },
    "ADVANCED": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 120,  # 2 minutos
        "pierdes": 3,
        "idioma": idioma_actual,
        "v1": 2,
        "v1,1": 3,
        "v2": 4,
        "v2,1":5,
        "v3": 6,
        "v3,1": 7,
        "advanced": advanced,
        "niv":3
    }
}
#sa
velocidad = {
     "BEGGINER": {
        "v1": 0,
        "v1,1": 1,
        "v2": 1,
        "v2,1": 2,
        "v3": 2,
        "v3,1": 3,
        "vel": 7
    },
    "INTERMEDIATE": {
        "v1": 1,
        "v1,1": 2,
        "v2": 2,
        "v2,1": 3,
        "v3": 3,
        "v3,1": 4,
        "vel": 7
    },
    "ADVANCED": {
        "v1": 2,
        "v1,1": 3,
        "v2": 4,
        "v2,1":5,
        "v3": 6,
        "v3,1": 7,
        "vel": 7
    }
}

def actualizar_niveles_config():
    global niveles_config
    niveles_config = {
    "BEGGINER": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 300,  # 5 minutos
        "pierdes": 7,
        "idioma": idioma_actual,
        "v1": 0,
        "v1,1": 1,
        "v2": 1,
        "v2,1": 2,
        "v3": 2,
        "v3,1": 3,
        "advanced": advanced,
        "niv":1
    },
    "INTERMEDIATE": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 200,  # 3 minutos y 20 segundos
        "pierdes": 5,
        "idioma": idioma_actual,
        "v1": 1,
        "v1,1": 2,
        "v2": 2,
        "v2,1": 3,
        "v3": 3,
        "v3,1": 4,
        "advanced": advanced,
        "niv":2
    },
    "ADVANCED": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 120,  # 2 minutos
        "pierdes": 3,
        "idioma": idioma_actual,
        "v1": 2,
        "v1,1": 3,
        "v2": 4,
        "v2,1":5,
        "v3": 6,
        "v3,1": 7,
        "advanced": advanced,
        "niv":3
    }
    }
def niveles(advanced, niv):
    if niv == 1:
        advanced
        sp1 = 0
        sp2 = 1
        sp3 = 2
        sp4 = 3
        objetos(sp1, sp2, sp3, sp4)
        circulos = 10
        cuadrados = 10
        tiempo_limite = 300
        pierdes = 7
        niv = 1
    if niv == 2:
        sp1 = 1
        sp2 = 2
        sp3 = 3
        sp4 = 4
        objetos(sp1, sp2, sp3, sp4)
        circulos = 10
        cuadrados = 10
        tiempo_limite = 200
        pierdes = 5
        niv = 2
    if niv == 3:
        sp1 = 2
        sp2 = 3
        sp3 = 4
        sp4 = 5
        objetos(sp1, sp2, sp3, sp4)
        circulos = 10
        cuadrados = 10
        tiempo_limite = 150
        pierdes = 3
        niv = 3
    if niv >= 4:
        if advanced == 0:
           levels_begginer()
        if advanced == 1:
            levels_advanced()
    resultado = juego(circulos, cuadrados, tiempo_limite, pierdes, idioma_actual, advanced, niv)
    if resultado == "reiniciar":
       niveles(advanced, niv)
    if resultado == "sig":
       niv += 1
       niveles(advanced, niv)
    if resultado == "volver":
        if advanced == 0:
           levels_begginer()
        if advanced == 1:
            levels_advanced
# Diccionarios para manejar los idiomas
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
    }
}

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guardians the Ocean")
icon = pygame.image.load("img/LogoG.png")
icon = pygame.transform.scale(icon, (icon.get_width() * 10, icon.get_height() * 10))
pygame.display.set_icon(icon)

fondo = pygame.image.load("img/fondo_dia.png")
fondo_escalado = pygame.transform.scale(fondo, (800, 600))

fondo1 = pygame.image.load("img/fondo_noche.png")
fondo_escalado = pygame.transform.scale(fondo1, (800, 600))

BG = pygame.image.load("img/fondo.jpg")
nuevo_tamaño = (800, 600)  # Cambia estos valores al tamaño deseado
# Escalar la imagen al nuevo tamaño
BG_escalado = pygame.transform.scale(BG, nuevo_tamaño)

BGC = pygame.image.load("img/instruesp1.jpeg")
nuevo_tamaño = (800, 600)  # Cambia estos valores al tamaño deseado
# Escalar la imagen al nuevo tamaño
BGC_escalado = pygame.transform.scale(BGC, nuevo_tamaño)

BGA = pygame.image.load("img/fondo_nivs2.jpg")
# Escalar la imagen al nuevo tamaño
BGA_escalado = pygame.transform.smoothscale(BGA, (800, 600))


hover = pygame.mixer.Sound("img/hover.mp3")
pygame.mixer.music.load("img/music.wav")
musiquita = pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
sound_playing = True

def get_btn(size):
    btn_image1 = pygame.image.load("img/button.png")
    btn_image2 = pygame.image.load("img/btn2.png")
    btn_image3 = pygame.image.load("img/btn3.png")
    resized_image1 = pygame.transform.scale(btn_image1, size)
    resized_image2 = pygame.transform.scale(btn_image2, size)
    resized_image3 = pygame.transform.scale(btn_image3, size)
    return resized_image1

button_size1 = (310, 80)
button_image1 = get_btn(button_size1)
#button_pos1 = (350, 250)
button_size2 = (310, 80)
button_image2 = get_btn(button_size2)
#button_pos2 = (350, 280)
button_size3 = (310, 80)
button_image3 = get_btn(button_size3)
#button_pos3 = (350, 310)

def get_fondoicon(size):
 fondoicon_image = pygame.image.load("img/ojo.png")
 resized_imagei = pygame.transform.scale(fondoicon_image, size)
 return resized_imagei

buttoni_size = (740, 395)
buttoni_image = get_fondoicon(buttoni_size)
buttoni_pos = (380, 223)

def get_fondoatras(size):
 fondoatras_image = pygame.image.load("img/fondo_atras.png")
 resized_imagea = pygame.transform.scale(fondoatras_image, size)
 return resized_imagea

buttona_size = (185, 80)
buttona_image = get_fondoatras(buttona_size)
buttona_pos = (35, 515)

def get_playatras(size):
 playatras_image = pygame.image.load("img/play_atras.png")
 resized_imageplay = pygame.transform.scale(playatras_image, size)
 return resized_imageplay

buttonp_size = (95, 95)
buttonp_image = get_playatras(buttonp_size)
buttonp_pos = (140, 255)

def get_usatras(size):
 usatras_image = pygame.image.load("img/us_atras.png")
 resized_imageus = pygame.transform.scale(usatras_image, size)
 return resized_imageus

buttonu_size = (95, 95)
buttonu_image = get_usatras(buttonu_size)
buttonu_pos = (140, 370)

def get_quitaratras(size):
 quitaratras_image = pygame.image.load("img/quitar_atras.png")
 resized_imagequitar = pygame.transform.scale(quitaratras_image, size)
 return resized_imagequitar

buttonq_size = (95, 95)
buttonq_image = get_quitaratras(buttonq_size)
buttonq_pos = (140, 480)

def get_btnplay(size):
 btnbeg_image = pygame.image.load("img/btnnivss.png")
 resized_imagebeg = pygame.transform.smoothscale(btnbeg_image, (350, 100))
 return resized_imagebeg

buttonbeg_size = (380, 150)
buttonbeg_image = get_btn(buttonbeg_size)



def get_btnb(size):
 btnb_image = pygame.image.load("img/rueda-de-engranajea.png")
 resized_imageb = pygame.transform.smoothscale(btnb_image, (80, 80))
 return resized_imageb

buttonb_size = (70, 70)
buttonb_image = get_btnb(buttonb_size)


def get_btns(size): 
 btns_image = pygame.image.load("img/sonidoa.png")
 resized_images = pygame.transform.smoothscale(btns_image, (80, 80))
 return resized_images

buttons_size = (70, 70)
buttons_image = get_btns(buttons_size)

sound_on_image = get_btns(buttons_size)

def get_btnns(size): 
 btnns_image = pygame.image.load("img/sin-sonidoa.png")
 resized_image = pygame.transform.smoothscale(btnns_image, (80, 80))
 return resized_image

buttonns_size = (70, 70)
buttonns_image = get_btnns(buttonns_size)

sound_off_image = get_btnns(buttonns_size)


def get_btnc(size): 
 btnc_image = pygame.image.load("img/jugando-videojuegoa.png")
 resized_imagec = pygame.transform.smoothscale(btnc_image, (90, 90))
 return resized_imagec

buttonc_size = (70, 70)
buttonc_image = get_btnc(buttonc_size)

def get_español(size): 
 btnes_image = pygame.image.load("img/español.png")
 resized_imagees = pygame.transform.scale(btnes_image, size)
 return resized_imagees

buttones_size = (180, 180)
buttones_image = get_español(buttones_size)

def get_ingles(size): 
 btnen_image = pygame.image.load("img/ingles.png")
 resized_imageen = pygame.transform.scale(btnen_image, size)
 return resized_imageen

buttonen_size = (180, 180)
buttonen_image = get_ingles(buttonen_size)

sound_on_image = get_btns(buttons_size)
sound_off_image = get_btnns(buttonns_size)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/Bakery.ttf", size)

def get_font1(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/Water.ttf", size)

def get_font2(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/easvhs.ttf", size)


def play():
    global sound_playing
    global p
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        p=2
        SCREEN.fill("black")
        SCREEN.blit(BGA_escalado, (0, 0))
        
        # Texto de "LEVELS" según el idioma
        PLAY_TEXT = get_font(90).render(textos[idioma_actual]["levels"], True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 150))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(buttoni_image, buttoni_pos)


        BEGGINER_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 290), 
                            text_input=textos[idioma_actual]["begginer"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        ADVANCED_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 420), 
                            text_input=textos[idioma_actual]["advanced"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=get_btnb(buttonb_size), pos=(750, 520), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 420), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 330), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(100, 550), 
                            text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="Blue", hovering_color="White")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN) 
        
        for button in [BEGGINER_BUTTON, ADVANCED_BUTTON, SOUND_BUTTON, CONTROL_BUTTON, SETTINGS_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.hoverEffect(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BEGGINER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    hover.play()
                    levels_begginer()
                if ADVANCED_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    hover.play()
                    levels_advanced()
                if CONTROL_BUTTON.checkForInput(PLAY_MOUSE_POS):
                  hover.play()
                  controls()
                if SETTINGS_BUTTON.checkForInput(PLAY_MOUSE_POS):
                  hover.play()
                  settings()
                if SOUND_BUTTON.checkForInput(PLAY_MOUSE_POS):
                  hover.play()
                  sound_playing = not sound_playing

                  if sound_playing:
                        pygame.mixer.music.unpause()  # Resume the music
                        
                  else:
                        pygame.mixer.music.pause()  # Pause the music

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                  hover.play()
                  main_menu()
                       
        pygame.display.update()

def levels_begginer():
   global sound_playing
   global advanced
   global p
   advanced = 0
   while True:
        LEVELSB_MOUSE_POS = pygame.mouse.get_pos()
        p=3
        SCREEN.fill("black")
        SCREEN.blit(BGA_escalado, (0, 0))
        
        LEVELSB_TEXT = get_font(90).render(textos[idioma_actual]["begginer"], True, "white")
        LEVELSB_RECT = LEVELSB_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(buttoni_image, buttoni_pos)

        SCREEN.blit(LEVELSB_TEXT, LEVELSB_RECT)

        LEVEL1_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 260), 
                            text_input=textos[idioma_actual]["level1"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 370), 
                            text_input=textos[idioma_actual]["level2"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 480), 
                            text_input=textos[idioma_actual]["level3"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=get_btnb(buttonb_size), pos=(750, 520), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 420), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 330), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVELSB_BACK = Button(image=None, pos=(100, 550), 
                             text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="Blue", hovering_color="White")
        LEVELSB_BACK.changeColor(LEVELSB_MOUSE_POS)
        LEVELSB_BACK.update(SCREEN) 

        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, SETTINGS_BUTTON,SOUND_BUTTON,CONTROL_BUTTON]:
            button.changeColor(LEVELSB_MOUSE_POS)
            button.hoverEffect(LEVELSB_MOUSE_POS)
            button.update(SCREEN)
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if LEVEL1_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                    niv = 1

                    niveles(advanced, niv)

                  #subprocess.Popen(["python", "objetos.py", str(vel["v1"]), str(vel["v1,1"]), str(vel["v2"]), str(vel["v2,1"]), str(vel["v3"]), str(vel["v3,1"]), str(vel["vel"])]) 

                if LEVEL2_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                    niv = 2
                
                    niveles(advanced, niv)

                  #subprocess.Popen(["python", "objetos.py", str(vel["v1"]), str(vel["v1,1"]), str(vel["v2"]), str(vel["v2,1"]), str(vel["v3"]), str(vel["v3,1"]), str(vel["vel"])])

                if LEVEL3_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                    niv = 3

                    niveles(advanced, niv)

                  #subprocess.Popen(["python", "objetos.py", str(vel["v1"]), str(vel["v1,1"]), str(vel["v2"]), str(vel["v2,1"]), str(vel["v3"]), str(vel["v3,1"]), str(vel["vel"])])

                if CONTROL_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                  hover.play()
                  controls()
                if SETTINGS_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                  hover.play()
                  settings()
                if SOUND_BUTTON.checkForInput(LEVELSB_MOUSE_POS):
                  hover.play()
                  sound_playing = not sound_playing

                  if sound_playing:
                        pygame.mixer.music.unpause()  # Resume the music
                        
                  else:
                        pygame.mixer.music.pause()  # Pause the music
            
                       
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELSB_BACK.checkForInput(LEVELSB_MOUSE_POS):
                  hover.play()
                  play()
        
        pygame.display.update()

def levels_advanced():
    global sound_playing
    global advanced
    global p
    advanced = 1

    while True:
        LEVELSA_MOUSE_POS = pygame.mouse.get_pos()
        p=4  
        SCREEN.fill("black")
        SCREEN.blit(BGA_escalado, (0, 0))
        
        LEVELSA_TEXT = get_font(90).render(textos[idioma_actual]["advanced"], True, "White")
        LEVELSA_RECT = LEVELSA_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(buttoni_image, buttoni_pos)


        SCREEN.blit(LEVELSA_TEXT, LEVELSA_RECT)

        LEVEL1_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 260), 
                               text_input=textos[idioma_actual]["level1"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 370), 
                               text_input=textos[idioma_actual]["level2"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 480), 
                               text_input=textos[idioma_actual]["level3"], font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=buttonb_image, pos=(750, 520), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 420), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 330), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        LEVELSA_BACK = Button(image=None, pos=(100, 550), 
                               text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="Blue", hovering_color="White")
        
        LEVELSA_BACK.changeColor(LEVELSA_MOUSE_POS)
        LEVELSA_BACK.update(SCREEN)  

        # Actualización de botones
        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, SETTINGS_BUTTON, SOUND_BUTTON, CONTROL_BUTTON]:
            button.changeColor(LEVELSA_MOUSE_POS)
            button.hoverEffect(LEVELSA_MOUSE_POS)
            button.update(SCREEN)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Comprobación de los niveles
                if LEVEL1_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    niv = 1

                    niveles(advanced, niv)              

                elif LEVEL2_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    niv = 2

                    niveles(advanced, niv)

                elif LEVEL3_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    niv = 3

                    niveles(advanced, niv)

                # Configuración y sonido
                if CONTROL_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    hover.play()
                    controls()
                if SETTINGS_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    hover.play()
                    settings()
                if SOUND_BUTTON.checkForInput(LEVELSA_MOUSE_POS):
                    hover.play()
                    sound_playing = not sound_playing
                    if sound_playing:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELSA_BACK.checkForInput(LEVELSA_MOUSE_POS):
                    hover.play()
                    play()

        pygame.display.update()

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(50).render(textos[idioma_actual]["about"], True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(100, 550), 
                            text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="Black", hovering_color="blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    hover.play()
                    main_menu()

        pygame.display.update()

def controls():
   global p
   while True:
        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("white")
        SCREEN.blit(BGC_escalado, (0, 0))

       # CONTROLS_TEXT = get_font(90).render(textos[idioma_actual]["controls"], True, "Black")
        #CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=(400, 100))
        #SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        CONTROLS_BACK = Button(image=None, pos=(100, 550), 
                            text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="Black", hovering_color="blue")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                    if p == 1:
                        hover.play()
                        main_menu()
                    if p == 2:
                        hover.play()
                        play()
                    if p == 3:
                        hover.play()
                        levels_begginer()
                    if p == 4:
                        hover.play()
                        levels_advanced()
        pygame.display.update()

def settings():
    global idioma_actual
    global p
    while True:
        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

        if p == 1:
         SCREEN.fill("white")
         SCREEN.blit(BG_escalado, (0, 0))
         SCREEN.blit(buttona_image, buttona_pos)
        if p == 2:
         SCREEN.fill("black")
         SCREEN.blit(BGA_escalado, (0, 0))
         SCREEN.blit(buttona_image, buttona_pos)
        if p == 3:
         SCREEN.fill("black")
         SCREEN.blit(BGA_escalado, (0, 0))
         SCREEN.blit(buttona_image, buttona_pos)
        if p == 4:
         SCREEN.fill("black")
         SCREEN.blit(BGA_escalado, (0, 0))
         SCREEN.blit(buttona_image, buttona_pos)

        # Texto de "Language" según el idioma
        OPTIONS_TEXT = get_font(90).render(textos[idioma_actual]["language"], True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
       
        ES_BUTTON = Button(image=get_español(buttones_size), pos=(220, 300), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        EN_BUTTON = Button(image=get_ingles(buttonen_size), pos=(550, 300), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BACK = Button(image=None, pos=(120, 550), 
                            text_input=textos[idioma_actual]["back"], font=get_font(50), base_color="white", hovering_color="blue")
        
        SETTINGS_BACK.changeColor(SETTINGS_MOUSE_POS)
        SETTINGS_BACK.update(SCREEN)

        for button in [ES_BUTTON, EN_BUTTON]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.hoverEffect(SETTINGS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ES_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    idioma_actual = "es"  # Cambiar a español
                    actualizar_niveles_config()  # Actualizar la configuración de niveles
                if EN_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    idioma_actual = "en"  # Cambiar a inglés
                    actualizar_niveles_config()  # Actualizar la configuración de niveles
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    if p == 1:
                        hover.play()
                        main_menu()
                    if p == 2:
                        hover.play()
                        play()
                    if p == 3:
                        hover.play()
                        levels_begginer()
                    if p == 4:
                        hover.play()
                        levels_advanced()

        pygame.display.update()


def draw_text_with_shadow_and_outline(text, font, pos, text_color, outline_color, shadow_color, letter_spacing=7):
    x, y = pos

    main_text = font.render(text, True, text_color)
    for letter in text:
        # Desplazamientos para el contorno
        offsets = [
            (-4, 0), (4, 0), (0, -4), (0, 4),  # Nivel 1
            (-3, -3), (-3, 3), (3, -3), (3, 3),  # Nivel 2 (diagonales)
            (-5, 0), (5, 0), (0, -5), (0, 5),   # Nivel 3
            (-6, 0), (6, 0), (0, -6), (0, 6)    # Nivel 4 para mayor grosor
        ]

        # Primero dibujar el contorno (desplazado en varias direcciones)
        for dx, dy in offsets:
            outline_text = font.render(letter, True, outline_color)
            SCREEN.blit(outline_text, (x + dx, y + dy))

        # Luego dibujar la sombra, ligeramente desplazada (por ejemplo, a la derecha y abajo)
        shadow_text = font.render(letter, True, shadow_color)
        SCREEN.blit(shadow_text, (x + 3, y + 3))  # Ajusta el desplazamiento de la sombra según lo necesites

        # Finalmente, dibujar el texto principal en su posición exacta
        main_text = font.render(letter, True, text_color)
        SCREEN.blit(main_text, (x, y))

        # Avanzar en la posición x para la siguiente letra con espaciado
        x += font.size(letter)[0] + letter_spacing

# En tu función del menú, puedes llamar a esta función de la siguiente manera:
def main_menu():
    global sound_playing
    global p
    
    while True:
        SCREEN.blit(BG_escalado, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        p = 1

        MENU_TEXT1 = get_font(60).render("THE", True, "#F2637E")
        MENU_TEXT2 = get_font(95).render("GUARDIANS", True, "white")
        MENU_TEXT3 = get_font(70).render("of", True, "#5D3FD3")
        MENU_TEXT4 = get_font(70).render("THE OCEAN", True, "#0A6AA6")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(150, 115))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(450, 115))
        MENU_RECT3 = MENU_TEXT3.get_rect(center=(200, 195))
        MENU_RECT4 = MENU_TEXT3.get_rect(center=(290, 195))

        SCREEN.blit(buttoni_image, buttoni_pos)
        SCREEN.blit(buttonp_image, buttonp_pos)
        SCREEN.blit(buttonu_image, buttonu_pos)
        SCREEN.blit(buttonq_image, buttonq_pos)


        PLAY_BUTTON = Button(image=get_btn(button_size1), pos=(400, 305), 
                        text_input=textos[idioma_actual]["play"], font=get_font(50), base_color="white", hovering_color="#F2637E")
        OPTIONS_BUTTON = Button(image=get_btn(button_size2), pos=(400, 415), 
                            text_input=textos[idioma_actual]["about"], font=get_font(50), base_color="white", hovering_color="#F2637E")
        SETTINGS_BUTTON = Button(image=get_btnb(buttonb_size), pos=(750, 520), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 420), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 330), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=get_btn(button_size3), pos=(400, 520), 
                            text_input=textos[idioma_actual]["quit"], font=get_font(50), base_color="white", hovering_color="#F2637E")
        
        SCREEN.blit(MENU_TEXT3, MENU_RECT3)
        SCREEN.blit(MENU_TEXT1, MENU_RECT1)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)
        SCREEN.blit(MENU_TEXT4, MENU_RECT4)


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SETTINGS_BUTTON, SOUND_BUTTON, CONTROL_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.hoverEffect(MENU_MOUSE_POS)
            button.update(SCREEN)

            #PLAY_BUTTON.hoverEffect(MENU_MOUSE_POS)        
            #OPTIONS_BUTTON.hoverEffect(MENU_MOUSE_POS)
            #QUIT_BUTTON.hoverEffect(MENU_MOUSE_POS)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hover.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hover.play()
                    options()
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hover.play()
                    settings()
                if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                 hover.play()
                 sound_playing = not sound_playing
                   
                 if sound_playing:
                        pygame.mixer.music.unpause()  # Resume the music
                 else:
                        pygame.mixer.music.pause()  # Pause the music

                if CONTROL_BUTTON.checkForInput(MENU_MOUSE_POS):
                  hover.play()
                  controls() 
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hover.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()