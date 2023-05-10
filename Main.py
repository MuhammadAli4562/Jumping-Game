# Importing modules
import pygame
import random
import math
# Initializing pygame
pygame.init()
# Setting up pygame screen
pygame.display.set_caption('Jumping Game')
# Screen size
width = 1000
height = 400
screen = pygame.display.set_mode((width, height))
# Draw image


def image(name, x, y):
    screen.blit(name, (x, y))


# Game Components
# Floor
background = pygame.image.load('src/background.png')
horse = pygame.image.load('src/frames/1.png')
backgroundX = 0
backgroundWidth = 1000
# Obstacle
obstacle = pygame.image.load('src/obstacle.jpg')
obstacleX = 1000
obstacleY = 267.5
# Horse
frames = ['src/frames/1.png', 'src/frames/2.png', 'src/frames/3.png', 'src/frames/4.png', 'src/frames/5.png', 'src/frames/6.png',
          'src/frames/7.png', 'src/frames/8.png', 'src/frames/9.png', 'src/frames/10.png', 'src/frames/11.png', 'src/frames/12.png',]
totalFrames = 12
horseX = 100
horseY = 250
horseY_change = 0


def horseMovement(frame, y):
    image = pygame.image.load(frames[int(frame)])
    if frame <= 1:
        screen.blit(image, (98, y))
    elif frame <= 2:
        screen.blit(image, (100, y))
    elif frame <= 3:
        screen.blit(image, (100, y))
    elif frame <= 4:
        screen.blit(image, (100, y))
    elif frame <= 5:
        screen.blit(image, (100, y))
    elif frame <= 6:
        screen.blit(image, (105, y))
    elif frame <= 7:
        screen.blit(image, (92, y-5))
    elif frame <= 8:
        screen.blit(image, (92, y-5))
    elif frame <= 9:
        screen.blit(image, (92, y-5))
    elif frame <= 10:
        screen.blit(image, (92, y-5))
    elif frame <= 11:
        screen.blit(image, (92, y-5))
    elif frame <= 12:
        screen.blit(image, (98, y-5))


# Game over
gameover = pygame.image.load('src/gameover.png')


def collision(obstacleX, obstacleY, horseX, horseY):
    horse_rect = horse.get_rect(center=(horseX, horseY))
    obstacle_rect = obstacle.get_rect(center=(obstacleX, obstacleY))
    if obstacle_rect.colliderect(horse_rect) == 1:
        return True


# Running pygame screen until escape condition
running = True
while running:
    # For filling screen with any colour using RGB
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Adding floor image and controlling its movement speed
    screen.blit(background, (backgroundX, 0))
    backgroundWidth -= 1
    screen.blit(background, (backgroundWidth, 0))
    backgroundX -= 1
    if backgroundX <= -1000:
        backgroundX = 0
        backgroundWidth = 1000
    # Checking all the event occurred while single iteration of while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Events of pressing keys
        if event.type == pygame.KEYDOWN:
            # Changes horses co-ordinates on pressing respective keys
            if event.key == pygame.K_SPACE and horseY == 250:
                horseY_change = -1
    # Horse movement frames and speed
    if totalFrames >= 12:
        totalFrames = 0
    horseY += horseY_change
    if horseY < 150:
        horseY = 150
        horseY_change = 0.5
    elif horseY > 250:
        horseY = 250
    # Horse movement
    horseMovement(totalFrames, horseY)
    totalFrames += 0.03
    # Obstacle movement
    screen.blit(obstacle, (obstacleX, obstacleY))
    obstacleX -= 3
    if obstacleX <= 0:
        obstacleX = 1000
    # Check for any collision
    if collision(obstacleX, obstacleY, horseX, horseY):
        screen.blit(gameover, (350, 150))
        pygame.display.update()
        running = False
        pygame.time.delay(1000)
    # Updating screen on each iteration
    pygame.display.update()
