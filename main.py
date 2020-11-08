import pygame
import random

# You always need to initialise pygame
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))  # Width, Height
background = pygame.image.load('background.jpg')
# 0,0 point in a top-left corner, 800, 600 in bottom, right corner

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("battleship.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("ship.png")
playerX = 370  # You have to include the size of the image itself
playerY = 480
playerX_change = 0

# Enemy
enemyIMG = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)  # You have to include the size of the image itself
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 30

# Bullet
bulletIMG = pygame.image.load("enemy.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"


# Ready - You can't see the bullet on the screen
# Fire - bullet on the screen

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))



def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


# Game loop
running = True
while running:
    # Background color RGB 0-255
    screen.fill((0, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Right/left right keystroke pressed?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # Always update screen or it won't work!
