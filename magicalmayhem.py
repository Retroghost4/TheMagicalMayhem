import pygame
import button
import random

Width, Height = 1500, 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("The Magical Mayhem")

BG = pygame.transform.scale(pygame.image.load("Mayhem1.jpg"), (Width, Height))
start_img = pygame.image.load('start.jpg').convert_alpha()

class Button():
  def __init__(self, x, y, image, scale): 
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height *scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False
    

  def draw(self): 
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos): 
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True 
    if pygame.mouse.get_pressed()[0] == 0: 
      self.clicked = False
    screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(375, 450, start_img, 0.8)
  
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

