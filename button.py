import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.original_image = image  # Store the original image for resetting size

        if self.image is None:
            self.image = self.text
        
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        # Display button image
        if self.image is not None:
            screen.blit(self.image, self.rect)
        # Display button text
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
         # Verifica si el mouse está dentro del rectángulo del botón
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        # Change text color if hovered
        if self.checkForInput(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def hoverEffect(self, position, hover_scale=1.05, max_scale=1.2):
        # Enlarge the button when the cursor hovers over it, not only on click
        if self.rect.collidepoint(position):  # Check if the cursor is over the button
            # Calcular el nuevo tamaño con el factor de escala
            new_width = int(self.rect.width * hover_scale)
            new_height = int(self.rect.height * hover_scale)
            
            # Limitar el tamaño máximo
            if new_width <= self.original_image.get_width() * max_scale:
                self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
            else:
                self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * max_scale), int(self.original_image.get_height() * max_scale)))
            
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            # Reset to the original size when not hovered
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
                
    def changeImage(self, new_image):
        self.image = new_image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	
  
        