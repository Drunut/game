import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1024, 768))
screen = pygame.display.set_mode((1024, 768), FULLSCREEN)

car = pygame.image.load('car.png')
screen.blit(car, (50,100))
pygame.display.flip()