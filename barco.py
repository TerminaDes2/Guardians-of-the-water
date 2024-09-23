import pygame

def cargar_barco():
    barco = pygame.image.load("barquito.png")# Cargar el sprite del barco
    barco = pygame.transform.scale(barco, (barco.get_width(), barco.get_height()))
    barco_rect = barco.get_rect()
    barco_rect.center = (400, 152)
    return barco, barco_rect
