from pygame import Surface
import pygame
from utils import start

def draw(display: Surface):
    #display.fill((255, 255, 255))
    pygame.draw.rect(display, color=(255, 0, 0),rect=(10, 10, 200, 200))

start(draw)