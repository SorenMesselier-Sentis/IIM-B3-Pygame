from turtle import width
import pygame
import random

class Pipe:
  def __init__(self):
    self.name = "Pipe"
    self.colorP = (0, 128, 0)
    self.widthP = 50
    self.heightP = random.randint(120, 500)
    self.downTry = self.heightP+120
    self.posX = 600
    self.posY = 0
    self.disparitionPosX = -5
    self.disP = False
  
  def Draw(self, screen, colorP, widthP):
    pygame.draw.rect(screen, colorP, (self.posX, 0, widthP, self.heightP))
    pygame.draw.rect(screen, (0, 128 , 0), (self.posX, self.downTry, widthP, 750-self.downTry))
    self.pipeSprite = pygame.image.load("pipe_green.png").convert_alpha()
    self.pipeSprite = pygame.transform.scale(self.pipeSprite, (self.widthP, self.heightP))
    self.pipeSprite = pygame.transform.rotate(self.pipeSprite, 180)
    screen.blit(self.pipeSprite, (self.posX, self.posY))

    self.pipeSpriteB = pygame.image.load("pipe_green.png").convert_alpha()
    self.pipeSpriteB = pygame.transform.scale(self.pipeSpriteB, (self.widthP, 750-self.downTry))
    screen.blit(self.pipeSpriteB, (self.posX, self.downTry))

  def colliderTopP(self, widthP):
    return pygame.Rect(self.posX, 0, widthP, self.heightP)

  def colliderBottomP(self, widthP):
    return pygame.Rect(self.posX, self.downTry, widthP, 750-self.heightP)