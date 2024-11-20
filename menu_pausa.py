import pygame
import sys

# Definir la función de pausa en este archivo
def mostrar_pausa(screen, btnsalida1, salida1_position, textos, idioma_actual):
    """
    Muestra el menú de pausa con un botón para regresar al menú principal.

    Args:
        screen (Surface): Pantalla del juego.
        btnmenu_image (Surface): Imagen del botón de Menú Principal.
        menu_position (tuple): Posición del botón de Menú Principal.
        textos (dict): Diccionario con los textos en diferentes idiomas.
        idioma_actual (str): Idioma actual seleccionado ("es" o "en").
    Returns:
        str: "salir" si se selecciona el botón de Menú Principal, de lo contrario None.
    """
    font = pygame.font.Font("img/Bakery.ttf", 80)
    paused = True

    while paused:
        screen.fill((0, 0, 0))  # Fondo oscuro o transparente para el menú de pausa

        # Mostrar el texto de "Pausa"
        texto_pausa = font.render(textos[idioma_actual]["pause"], True, (255, 255, 255))
        screen.blit(texto_pausa, (400, 200))  # Ajusta la posición según necesites

        # Mostrar el botón de Menú Principal
        screen.blit(btnsalida1, salida1_position)
        pygame.display.flip()

        # Manejar eventos de pausa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnsalida1.get_rect(topleft=salida1_position).collidepoint(pygame.mouse.get_pos()):
                    return "salir"  # Si se selecciona Menú Principal, regresa "salir"