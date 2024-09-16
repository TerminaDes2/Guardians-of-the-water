import pygame

def draw_triangle(surface, color, pos, size):
    point1 = (pos[0], pos[1])
    point2 = (pos[0] - size, pos[1] + size)
    point3 = (pos[0] + size, pos[1] + size)
    pygame.draw.polygon(surface, color, [point1, point2, point3])

def check_collision(triangle_pos, triangle_size, obj_pos, obj_size):
    triangle_rect = pygame.Rect(triangle_pos[0] - triangle_size, triangle_pos[1], triangle_size * 2, triangle_size)
    obj_rect = pygame.Rect(obj_pos[0], obj_pos[1], obj_size, obj_size)
    return triangle_rect.colliderect(obj_rect)
