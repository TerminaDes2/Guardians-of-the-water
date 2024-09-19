import pygame


def cargar_barco():
    barco = pygame.image.load("barco.png")# Cargar el sprite del barco
    barco = pygame.transform.scale(barco, (barco.get_width() * 4, barco.get_height() * 4))
    barco_rect = barco.get_rect()
    barco_rect.center = (400, 172)
    return barco, barco_rect
