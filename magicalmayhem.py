import pygame
import random

Width, Height = 2000, 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The Magical Mayhem")

def main(): 
  run = True
  while run: 
    for event in pygame.event.get(): 
      run = False
      break

  pygame.quit()

if __name__ = "__main__": 
  main()

