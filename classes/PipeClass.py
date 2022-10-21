import pygame
import random

class Pipe:
  def __init__(self):
    self.name = "Pipe"
    self.green = (0,255,0)
    self.widthF = 40
    self.heightF = 250
    self.posX = 400
    self.posY = 400
    self.rangeX = (0, 750)
    self.range = (300, 600)

  def Draw(self, screen, green, widthF, heightF):
    pygame.draw.rect(screen, green, (self.posX, self.posY, widthF, heightF))

  def RandomPipeBottom(self, screen, rangeX):
    x = random.randrange(rangeX)  

  def create(self, screen):
    pipeBase = screen/3
    pipeHeight = self.heightF
    y2 = screen + random.randrange( 0, int(screen - pipeHeight * pipeBase))  
    xPoint = screen + 20
    y1 = pipeHeight - y2 + pipeBase
    pipe = [
      {'x': xPoint, 'y': -y1},
      {'x': xPoint, 'y': y1}
    ]