import pygame,sys,os
from pygame.locals import *

red = [255,0,0]#(255,0,0)

#initialize pygame
pygame.init()

#setup window
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("SNAKE GAME")

#set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()
while True:
     print("hi")
