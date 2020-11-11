import pygame
import random
import math
from pygame import mixer
import os

# os.environ['SDL_AUDIODRIVER'] = 'dsp'
# You always need to initialise pygame
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))  # Width, Height
background = pygame.image.load('background.jpg')
# 0,0 point in a top-left corner, 800, 600 in bottom, right corner

# Background Sound
mixer.init()
mixer.music.load("Into_The_Breach.ogg")
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("battleship.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("ship.png")
playerX = 370  # You have to include the size of the image itself
playerY = 480
playerX_change = 0
player_mov_NULL = 0
player_mov_left = -0.8
player_mov_right = 0.8

# Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_mov_left = -0.5
enemy_mov_right = 0.5

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))  # You have to include the size of the image itself
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(30)

# Bullet
bulletIMG = []
bulletX = []
bulletY = []
bulletX_change = []
bulletY_change = []
bullet_state = []
num_of_bullets = 6

for i in range(num_of_bullets):
    bulletIMG.append(pygame.image.load("bullet.png"))
    bulletX.append(0)
    bulletY.append(480)
    bulletX_change.append(0)
    bulletY_change.append(0.8)
    bullet_state.append("ready")

# Score
score_value = 0
font = pygame.font.Font('Academic M54.ttf', 32)
textX = 10
textY = 10
num = 5

# Game over
over_font = pygame.font.Font('Academic M54.ttf', 64)


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text1 = over_font.render(f"GAME OVER", True, (255, 255, 255))
    over_text2 = over_font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(over_text1, (250, 250))
    screen.blit(over_text2, (290, 320))


# Ready - You can't see the bullet on the screen
# Fire - bullet on the screen

def fire_bullet(x, y, i):
    global bullet_state
    bullet_state[i] = "fire"
    screen.blit(bulletIMG[i], (x + 16, y + 10))


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                playerX_change = player_mov_left
            if event.key == pygame.K_RIGHT:
                playerX_change = player_mov_right
            if event.key == pygame.K_SPACE:
                for i in range(num_of_bullets):
                    if bullet_state[i] == "ready":
                        shot_sound = mixer.Sound('shot_sound.wav')
                        shot_sound.play()
                        bulletX[i] = playerX
                        fire_bullet(bulletX[i], playerY, i)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = player_mov_NULL

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            game_over_text()
            for j in range(num_of_enemies):
                enemyY[j] = 2000
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = enemy_mov_right
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = enemy_mov_left
            enemyY[i] += enemyY_change[i]
        # Collision
        for j in range(num_of_bullets):
            collision = isCollision(enemyX[i], enemyY[i], bulletX[j], bulletY[j])
            if collision:
                collision_sound = mixer.Sound('explosion_sound.wav')
                collision_sound.play()
                bulletY[j] = 480
                bullet_state[j] = "ready"
                score_value += 1
                # print(score_value)
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)
            enemy(enemyX[i], enemyY[i], i)
        # Bullet movement
        for i in range(num_of_bullets):
            if bulletY[i] <= 0:
                bulletY[i] = 480
                bullet_state[i] = "ready"

            if bullet_state[i] == "fire":
                fire_bullet(bulletX[i], bulletY[i], i)
                bulletY[i] -= bulletY_change[i]
    if score_value > num:
        num += 5
        num_of_enemies += 1
        for i in range(1):
            enemyIMG.append(pygame.image.load("enemy.png"))
            enemyX.append(random.randint(0, 735))  # You have to include the size of the image itself
            enemyY.append(random.randint(50, 150))
            enemyX_change.append(random.choice([enemy_mov_left, enemy_mov_right]))
            enemyY_change.append(30)
        enemy_mov_right += 0.1
        enemy_mov_left -= 0.1
        player_mov_right += 0.1
        player_mov_left -= 0.1
    # print(f' Round stats: enemy mov {enemyX_change[0]}, player mov {player_mov_right}')
    # if num_of_enemies > 10
    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()  # Always update screen or it won't work!
