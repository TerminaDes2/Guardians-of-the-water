import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("img/fondo.jpeg")
hover = pygame.mixer.Sound("img/hover.mp3")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/Bakery.ttf", size)

def get_font1(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/Water.ttf", size)

def get_font2(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/easvhs.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
        
        PLAY_TEXT = get_font(45).render("LEVELS", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        BEGGINER_BUTTON = Button(image=None, pos=(500, 360), 
                            text_input="BEGGINER", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        ADVANCED_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(500, 430), 
                            text_input="ADVANCED", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")


        PLAY_BACK = Button(image=None, pos=(100, 550), 
                            text_input="Back", font=get_font(50), base_color="White", hovering_color="yellow")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN) 
        
        for button in [BEGGINER_BUTTON, ADVANCED_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
               if BEGGINER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    print ("Hola")
                
        if ADVANCED_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    print ("Adios")

        if event.type == pygame.MOUSEBUTTONDOWN:
                  if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            

            
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(10).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 460), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()



        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
       

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT3 = get_font(117).render("THE GUARDIANS OF", True, "black")
        MENU_TEXT1 = get_font(110).render("THE GUARDIANS OF", True, "#FFD700")
        MENU_TEXT2 = get_font1(95).render("THE WATER", True, "#1E90FF")
        MENU_RECT3 = MENU_TEXT3.get_rect(center=(500, 150))
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(500, 150))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(500, 250))
       

        PLAY_BUTTON = Button(image=None, pos=(500, 360), 
                            text_input="PLAY", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(500, 430), 
                            text_input="OPTIONS", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(500, 500), 
                            text_input="QUIT", font=get_font2(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT3, MENU_RECT3)
        SCREEN.blit(MENU_TEXT1, MENU_RECT1)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)
      


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()