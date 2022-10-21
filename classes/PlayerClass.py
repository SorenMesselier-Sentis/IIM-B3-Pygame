import pygame

class Player:
  def __init__(self):
    self.name = "Flappy"
    self.flappySprite = pygame.image.load('./assets/flappy-bird.png').convert_alpha()
    self.test = (255, 0, 0)
    self.isJumping = False
    self.widthF = 50
    self.heightF = 30
    self.posX = 200
    self.posY = 680
    self.v = 6 # velocity
    self.m = 1 # mass
    self.isJumping = False

  def Draw(self, screen, test, widthF, heightF):
    pygame.draw.rect(screen, test, (self.posX, self.posY, widthF, heightF))

  def Jump(self):
    if self.isJumping:
      f = (1/2)*self.m*(self.v**2)
      self.posY -= f
      self.v = self.v-1

    if self.v < 0:
      self.m = -1
    
    if self.v == -7:
      self.isJumping = False
      self.v = 6
      self.m = 1