import pygame
from pygame.locals import *
import sys

def start(draw_func, title: str = "Window", width: int = 640, height: int = 480):

    pygame.init()
    pygame.display.set_caption(title)
    flags = pygame.RESIZABLE
    display = pygame.display.set_mode((width, height), flags=flags, vsync=1)

    while True:
        # Close on quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # F = full screen mode
            if event.type == pygame.KEYUP and event.key == K_f:
                pygame.display.toggle_fullscreen()

                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

        draw_func(display)
        
        pygame.display.update()
