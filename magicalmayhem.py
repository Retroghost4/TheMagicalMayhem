import pygame
import pygame_menu
from pygame_menu import themes
import sys
import random

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def start_the_mayhem(): 
  mainmenu_open(loading)
  pygame.time.set_timer(update_loading, 30)

mainmenu = pygame_menu.Menu('Welcome...' , 500, 300, 
                        theme=pygame_menu.themes.THEME_RED)
mainmenu.add.text_input('Name: ', default='Mortal')
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

loading = pygame_menu.Menu('Commencing Mayhem...' 600, 400, theme=theme.THEME_DARK
loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width= 200)

while True: 
  events = pygame.event.get()
  for event in events: 
    if event.type == update_loading: 
      progress = loading.get_widget("1")
      progress.set_value(progress.get_value() + 1)
      if progress.get_value() == 100: 
        pygame.time.set_timer(update_loading, 0)
   
    if event.type == pygame.QUIT: 
      exit()
        
