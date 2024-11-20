import pygame

def cargar_barco():
    barco = pygame.image.load("img/barquito4.png")# Cargar el sprite del barco
    barco = pygame.transform.scale(barco, (barco.get_width(), barco.get_height()))
    barco_rect = barco.get_rect()
    barco_rect.center = (376, 190)
    return barco, barco_rect
