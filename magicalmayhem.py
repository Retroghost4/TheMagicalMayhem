import pygame
import pygame_menu
import sys
import random

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
menu = pygame_menu.Menu('Welcome...' , 500, 300, 
                        theme=pygame_menu.themes.THEME_RED)


while True: 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      pygame.quit()
      sys.exit()
