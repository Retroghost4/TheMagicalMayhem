import pygame, sys
from button import Button
import random

Width, Height = 1500, 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The Magical Mayhem")
BG = pygame.transform.scale(pygame.image.load("1.png"), (Width, Height))

  
def draw(): 
  window.blit(BG, (0, 0))
  pygame.display.update()

def main_menu(): 
  while True: 
    MENU_mouse_pos = pygame.mouse.get_pos()
    PLAY_button = Button(image=pygame.image.load('play button.png'), pos=(375, 450))
    for button in (PLAY_button):
       button.update(window)

def main(): 
  run = True
  while run: 
      
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        run = False
      break

    draw()

  pygame.quit()

if __name__ == "__main__": 
  main()

