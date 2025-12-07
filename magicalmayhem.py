import pygame
import button
import random

Width, Height = 1500, 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The Magical Mayhem")

BG = pygame.transform.scale(pygame.image.load("Mayhem1.jpg"), (Width, Height))
start_img = pygame.image.load('start.jpg').convert_alpha()


start_button = button.Button(375, 450, start_img, 0.8)
  
def draw(): 
  window.blit(BG, (0, 0))
  pygame.display.update()

def main(): 
  run = True
  while run: 
    if start_button.draw(screen): 
      print ('Start')
      
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        run = False
      break

    draw()

  pygame.quit()

if __name__ == "__main__": 
  main()

