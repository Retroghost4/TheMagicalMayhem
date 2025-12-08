import pygame
import random

def main_menu():
  pygame.display.set_caption("The Magical Mayhem")
  while True: 
    window.blit(BG, (0, 0))

    MENU_MOUSE_POS =  pygame.mouse.get_pos()
    PLAY_BUTTON = Button(image=pygame.image.load('play button.png'), pos=(375, 450)

Width, Height = 1500, 900
window = pygame.display.set_mode((Width, Height))


BG = pygame.transform.scale(pygame.image.load("1.png"), (Width, Height))


  
def draw(): 
  window.blit(BG, (0, 0))
  pygame.display.update()

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

