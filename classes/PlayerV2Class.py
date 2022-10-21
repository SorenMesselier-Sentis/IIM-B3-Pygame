import pygame

class Player:
  def __init__(self):
    self.name = "Flappy"
    self.colorF = (255, 0, 0)
    self.widthF = 50
    self.heightF = 30
    self.posX = 50
    self.posY = 325
    self.newYPose = 0

  def Draw(self, screen, colorF, widthF, heightF):
    pygame.draw.rect(screen, colorF, (self.posX, self.posY, widthF, heightF))
    self.flappySprite = pygame.image.load("flappy_bird.png").convert_alpha()
    self.flappySprite = pygame.transform.scale(self.flappySprite, (self.widthF, self.heightF))
    screen.blit(self.flappySprite, (self.posX, self.posY))

  def colliderF(self):
    return pygame.Rect(self.posX, self.posY, self.widthF, self.heightF)