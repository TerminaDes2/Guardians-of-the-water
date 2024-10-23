import subprocess
import pygame, sys
from button import Button

pygame.init()

# Diccionario con configuraciones de los niveles
niveles_config = {
    "BEGGINER": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 300,  # 5 minutos
        "pierdes": 7
    },
    "INTERMEDIATE": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 200,  # 3 minutos y 20 segundos
        "pierdes": 5
    },
    "ADVANCED": {
        "circulos": 10,
        "cuadrados": 10,
        "tiempo_limite": 120,  # 2 minutos
        "pierdes": 3
    }
}

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("img/bg.jpeg")
BGA = pygame.image.load("img/i.jpg")
hover = pygame.mixer.Sound("img/hover.mp3")
pygame.mixer.music.load("img/music.wav")
musiquita = pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
sound_playing = True

def get_btn(size):
    btn_image1 = pygame.image.load("img/btn1.png")
    btn_image2 = pygame.image.load("img/btn2.png")
    btn_image3 = pygame.image.load("img/btn3.png")
    resized_image1 = pygame.transform.scale(btn_image1, size)
    resized_image2 = pygame.transform.scale(btn_image2, size)
    resized_image3 = pygame.transform.scale(btn_image3, size)
    return resized_image1

button_size1 = (260, 70)
button_image1 = get_btn(button_size1)
#button_pos1 = (350, 250)
button_size2 = (260, 70)
button_image2 = get_btn(button_size2)
#button_pos2 = (350, 280)
button_size3 = (260, 70)
button_image3 = get_btn(button_size3)
#button_pos3 = (350, 310)

def get_btnplay(size):
 btnbeg_image = pygame.image.load("img/btnbeg.png")
 resized_imagebeg = pygame.transform.scale(btnbeg_image,size)
 return resized_imagebeg

buttonbeg_size = (260, 100)
buttonbeg_image = get_btn(buttonbeg_size)
button_pos = (350, 250)

def get_btnb(size):
 btnb_image = pygame.image.load("img/settings.png")
 resized_imageb = pygame.transform.scale(btnb_image, size)
 return resized_imageb

buttonb_size = (60, 60)
buttonb_image = get_btnb(buttonb_size)

def get_btns(size): 
 btns_image = pygame.image.load("img/sound.png")
 resized_images = pygame.transform.scale(btns_image, size)
 return resized_images

buttons_size = (60, 60)
buttons_image = get_btns(buttons_size)

sound_on_image = get_btns(buttons_size)


def get_btnns(size): 
 btnns_image = pygame.image.load("img/nosound.png")
 resized_image = pygame.transform.scale(btnns_image, size)
 return resized_image

buttonns_size = (70, 70)
buttonns_image = get_btnns(buttonns_size)

sound_off_image = get_btnns(buttonns_size)

sound_playing = True  # Initially, the sound is playing


def get_btnc(size): 
 btnc_image = pygame.image.load("img/control.png")
 resized_imagec = pygame.transform.scale(btnc_image, size)
 return resized_imagec

buttonc_size = (70, 70)
buttonc_image = get_btnc(buttonc_size)

def get_español(size): 
 btnes_image = pygame.image.load("img/español.png")
 resized_imagees = pygame.transform.scale(btnes_image, size)
 return resized_imagees

buttones_size = (300, 150)
buttones_image = get_español(buttones_size)

def get_ingles(size): 
 btnen_image = pygame.image.load("img/ingles.png")
 resized_imageen = pygame.transform.scale(btnen_image, size)
 return resized_imageen

buttonen_size = (170, 170)
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
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("black")
        SCREEN.blit(BGA, (0, 0))
        
        PLAY_TEXT = get_font1(90).render("LEVELS", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        BEGGINER_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 260), 
                            text_input="BEGGINER", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        INTERMEDIATE_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 360), 
                            text_input="INTERMEDIATE", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        ADVANCED_BUTTON = Button(image=get_btnplay(buttonbeg_size), pos=(400, 460), 
                            text_input="ADVANCED", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=get_btnb(buttonb_size), pos=(750, 540), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 450), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 370), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(100, 550), 
                            text_input="Back", font=get_font(50), base_color="Blue", hovering_color="White")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN) 
        
        for button in [BEGGINER_BUTTON, ADVANCED_BUTTON, SETTINGS_BUTTON,SOUND_BUTTON,CONTROL_BUTTON,INTERMEDIATE_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.hoverEffect(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BEGGINER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    config = niveles_config["BEGGINER"]
                    subprocess.Popen(["python", "juego.py", str(config["circulos"]), str(config["cuadrados"]), str(config["tiempo_limite"]), str(config["pierdes"])])
                if INTERMEDIATE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    config = niveles_config["INTERMEDIATE"]
                    subprocess.Popen(["python", "juego.py", str(config["circulos"]), str(config["cuadrados"]), str(config["tiempo_limite"]), str(config["pierdes"])])
                if ADVANCED_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    config = niveles_config["ADVANCED"]
                    subprocess.Popen(["python", "juego.py", str(config["circulos"]), str(config["cuadrados"]), str(config["tiempo_limite"]), str(config["pierdes"])])

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
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        

        OPTIONS_TEXT = get_font(50).render("ABOUT US", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(100, 550), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="blue")

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
   while True:
        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        
        CONTROLS_TEXT = get_font(90).render("CONTROLS", True, "Black")
        CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        CONTROLS_BACK = Button(image=None, pos=(100, 550), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="blue")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                    hover.play()
                    main_menu()

        pygame.display.update()

def settings():
    while True:
        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(90).render("LANGUAGE", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
       
        ES_BUTTON = Button(image=get_español(buttones_size), pos=(300, 360), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        EN_BUTTON = Button(image=get_ingles(buttonen_size), pos=(500, 360), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BACK = Button(image=None, pos=(100, 550), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="blue")
        
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
                if EN_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                  print ("Hola")
                if ES_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                  print ("Hola")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    hover.play()
                    main_menu()
        SCREEN.blit(BG, (0, 0))

        pygame.display.update()

def main_menu():
    global sound_playing
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT1 = get_font(50).render("THE", True, "#F2637E")
        MENU_TEXT2 = get_font(95).render("GUARDIANS", True, "white")
        MENU_TEXT3 = get_font(60).render("of", True, "#FFA500")
        MENU_TEXT4 = get_font1(70).render("THE Ocean", True, "#0A6AA6")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(150, 115))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(450, 115))
        MENU_RECT3 = MENU_TEXT3.get_rect(center=(200, 195))
        MENU_RECT4 = MENU_TEXT3.get_rect(center=(290, 195))

        PLAY_BUTTON = Button(image=get_btn(button_size1), pos=(400, 305), 
                        text_input="PLAY", font=get_font2(35), base_color="white", hovering_color="White")
        OPTIONS_BUTTON = Button(image=get_btn(button_size2), pos=(400, 410), 
                            text_input="ABOUT", font=get_font2(35), base_color="white", hovering_color="White")
        SETTINGS_BUTTON = Button(image=get_btnb(buttonb_size), pos=(750, 540), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=sound_on_image if sound_playing else sound_off_image, pos=(750, 450), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        CONTROL_BUTTON = Button(image=get_btnc(buttonc_size), pos=(750, 370), 
                            text_input="", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=get_btn(button_size3), pos=(400, 520), 
                            text_input="QUIT", font=get_font2(35), base_color="white", hovering_color="White")

        SCREEN.blit(MENU_TEXT3, MENU_RECT3)
        SCREEN.blit(MENU_TEXT1, MENU_RECT1)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)
        SCREEN.blit(MENU_TEXT4, MENU_RECT4)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SETTINGS_BUTTON, SOUND_BUTTON, CONTROL_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.hoverEffect(MENU_MOUSE_POS)
            button.update(SCREEN)

            #PLAY_BUTTON.hoverEffect(MENU_MOUSE_POS)        
           # OPTIONS_BUTTON.hoverEffect(MENU_MOUSE_POS)
            #QUIT_BUTTON.hoverEffect(MENU_MOUSE_POS)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hover.play()
                    # Lanza juego.py como un nuevo proceso
                    #subprocess.Popen(["python", "juego.py"])
                    # Cierra el programa principal
                    #pygame.quit()
                    #sys.exit()
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