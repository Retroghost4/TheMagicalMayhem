import pygame
import random

Width, Height = 2000, 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The Magical Mayhem")

BG = pygame.transform.scale(pygame.image.load("Mayhem1.jpg"), (Width, Height))

def draw(): 
  window.blit(BG, (0, 0))
  pygame.display.update()

def main(): 
  run = True
  while run: 
    for event in pygame.event.get(): 
      run = False
      break

    draw()

  pygame.quit()

if __name__ == "__main__": 
  main()

