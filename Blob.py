import pygame
import random
import sys
 
# Initialize Pygame
pygame.init()
 
# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncy Growing Square")
 
# Font
font = pygame.font.SysFont(None, 80)
 
# Square
size = 50
square_color = (255, 0, 0)
center = (WIDTH // 2, HEIGHT // 2)
 
# Animation
bounce_scale = 1.0
bounce_target = 1.2
bounce_speed = 0.1
bouncing = False
 
# Clock
clock = pygame.time.Clock()
 
def get_random_color():
    while True:
        color = [random.randint(0, 255) for _ in range(3)]
        if color != [0, 0, 0]:  
            return tuple(color)
 
# loop
running = True
show_text = False
 
while running:
    screen.fill((0, 0, 0))
 
    # Determine current square size
    scaled_size = min(int(size * bounce_scale), WIDTH, HEIGHT)
    draw_top_left = (center[0] - scaled_size // 2, center[1] - scaled_size // 2)
    pygame.draw.rect(screen, square_color, (draw_top_left[0], draw_top_left[1], scaled_size, scaled_size))
 
    # Display "YAY" when max
    if show_text:
        text = font.render("YAY", True, (0, 0, 0))
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)
 
    pygame.display.flip()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        elif event.type == pygame.MOUSEBUTTONDOWN and not show_text:
            mouse_pos = pygame.mouse.get_pos()
            real_top_left = (center[0] - size // 2, center[1] - size // 2)
            square_rect = pygame.Rect(*real_top_left, size, size)
            if square_rect.collidepoint(mouse_pos):
                size += 80
                if size < max(WIDTH, HEIGHT):
                    square_color = get_random_color()
                bouncing = True
                bounce_scale = bounce_target
 
    if bouncing and not show_text:
        bounce_scale -= bounce_speed
        if bounce_scale <= 1.0:
            bounce_scale = 1.0
            bouncing = False
 
    # LOCK IN max size. trigger text
    if size >= max(WIDTH, HEIGHT):
        show_text = True
        size = max(WIDTH, HEIGHT)
        bounce_scale = 1.0
        bouncing = False
 
    clock.tick(60)
 
pygame.quit()
sys.exit()