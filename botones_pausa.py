# botones_pausa.py
import pygame
import sys

# Configuración de botones e imágenes
btnsalida = pygame.image.load("img/flecha.png")
btnreiniciar = pygame.image.load("img/actualizar.png")
btnsiguiente = pygame.image.load("img/proximo.png")
btnsalida1 = pygame.image.load("img/flecha.png")

btnsalida = pygame.transform.scale(btnsalida, (90, 90))
btnsalida1 = pygame.transform.scale(btnsalida1, (90, 90))
btnreiniciar = pygame.transform.scale(btnreiniciar, (90, 90))
btnsiguiente = pygame.transform.scale(btnsiguiente, (90, 90))

salida_position = (300, 300)
salida1_position = (500, 300)
reiniciar_position = (400, 300)
siguiente_position = (400, 300)

# Función para el botón de siguiente nivel
def siguiente_nivel(screen):
    while True:
        screen.blit(btnsiguiente, siguiente_position)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "salir"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnsiguiente.get_rect(topleft=siguiente_position).collidepoint(pygame.mouse.get_pos()):
                    return "salir"

# Función para mostrar la pausa
def mostrar_pausa(screen):
   en_pausa = True
   while en_pausa:
        screen.blit(btnsalida1, salida1_position)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnsalida1.get_rect(topleft=salida1_position).collidepoint(pygame.mouse.get_pos()):
                    return False  # Regresa False para salir de la pausa
   return True  # Regresa True si el ciclo de pausa no cambia

# Función para mostrar los botones de "Reiniciar" y "Salir"
def mostrar_botones(screen, en_pausa):
    while not en_pausa:
        screen.blit(btnreiniciar, reiniciar_position)
        screen.blit(btnsalida, salida_position)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "salir"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnreiniciar.get_rect(topleft=reiniciar_position).collidepoint(pygame.mouse.get_pos()):
                    return "reiniciar"
                elif btnsalida.get_rect(topleft=salida_position).collidepoint(pygame.mouse.get_pos()):
                    return "salir"
