# all import
import pygame
import random

# from import Player
from classes.PlayerV2Class import Player
from classes.PipeV2Class import Pipe

# init set up for the window and sound
pygame.init()
pygame.display.set_caption("Flappy bird")
screen = pygame.display.set_mode((600, 750))

# set up loop
loop = True
blue = (135,206,250)

# set up flappy
player = Player()

# set up pipe
pipe = Pipe()

# set up score
PipePass = 0
font = pygame.font.Font(None, 36)

# begining of the loop
while loop:

  screen.fill((blue))
 
# set up background music
  # pygame.mixer.init()
  # sound = pygame.mixer.Sound("/Undertale_Papyrus_Theme_Song_Bonetrousle.mp3")
  # sound.play()

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      loop = False 

# flappy movments
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_SPACE:
        player.newYPose = -8
        
    if e.type == pygame.KEYUP:
      if e.key == pygame.K_SPACE:
        player.newYPose = 6

  player.posY += player.newYPose

# border for flappy bird so he can't go out of the screen
  if player.posY <= 0: 
    player.posY = 0
  if player.posY >= 720: 
    player.posY = 750 - player.heightF

# Pipe generation
  pipe.posX += pipe.disparitionPosX
  if pipe.posX <= -5:
    pipe.posX = 600
    pipe.heightP = random.randint(100, 500)
    pipe.downTry = pipe.heightP+random.randint(80, 250)

# create collider for pipes
  colliderTopP = pipe.colliderTopP(widthP=50)
  colliderBottomP = pipe.colliderBottomP(widthP=50)

  if player.posX == pipe.posX:
    PipePass += 1

# check collision
  if player.colliderF().colliderect(colliderTopP):
    print('Score : '+str(PipePass))
    loop = False
  if player.colliderF().colliderect(colliderBottomP):
    print('Score : '+str(PipePass))
    loop = False

# Draw pipes and flappy
  pipe.Draw(screen, colorP=(135, 206, 250), widthP=50)
  player.Draw(screen, colorF=(135, 206,  250), widthF=50, heightF=30)

# Display score on the screen
  txt = font.render('Score : '+str(PipePass), 1, (0, 0, 0))
  screen.blit(txt,(450, 25))

  pygame.time.delay(20)
  pygame.display.flip()
pygame.quit()