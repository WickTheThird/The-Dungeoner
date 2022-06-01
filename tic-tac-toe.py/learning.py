#!/usr/bin/env python3

import pygame, random, math
pygame.init()

#screen
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('tic-tac-toe.py/spaceship.png')
background = pygame.image.load('tic-tac-toe.py/planet.png')

#player controls and spawn points
player_i = pygame.image.load('tic-tac-toe.py/spaceship_2.png')

playerX = 370
playerX_change = 0
playerY = 480
playerY_change = 0

def player(x, y):
    screen.blit(player_i, (x, y))


#player jet
jet_1 = pygame.image.load('tic-tac-toe.py/hot.png')
jet_2 = pygame.image.load('tic-tac-toe.py/hot.png')
jet_ready = False

def jet_fire(x, y):
    screen.blit(jet_1, (x + 18, y + 60))


def jet_fire_2(x, y):
    screen.blit(jet_2, (x + 30, y + 60))


#enemy control and spawn points
enemy_i = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemy_i.append(pygame.image.load('tic-tac-toe.py/monster.png'))
    enemyX.append(random.randint(0, 600))
    enemyX_change.append(3)
    enemyY.append(0)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemy_i[i], (x, y))


#bullet control and action
bullet = pygame.image.load('tic-tac-toe.py/bullet.png')

bulletX = 0
bulletX_change = 0
bulletY = playerY
bulletY_change = 100
bullet_state = "Ready!"

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "Fire!"
    screen.blit(bullet, (x + 23, y))


#collision detection
def isColision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 30:
        return True 
    else:
        return False


#name and icon
pygame.display.set_caption('Space Invadors')
pygame.display.set_icon(icon)

#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score_v = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_v, (x, y))


#game over
over_font = pygame.font.Font('freesansbold.ttf', 70)

def game_over():
    over_text = over_font.render('Game Over!', True, (255,255,255))
    screen.blit(over_text, (90, 250))


def isColision_2(playerX, playerY, enemyX, enemyY):
    distance_2 = math.sqrt((math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2)))
    if distance_2 < 40:
        return True
    else:
        return False

#you win
you_win = pygame.image.load('tic-tac-toe.py/you_win.webp')
def win():
    screen.blit(you_win, (150, 250))

#the ongoing game loop
ref = True
while ref == True:
    screen.fill((135, 206, 235))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ref = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
                jet_ready = True
            if event.key == pygame.K_UP:
                playerY_change = -10
                jet_ready = True
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
                jet_ready = True
            if event.key == pygame.K_DOWN:
                playerY_change = 10
                jet_ready = True
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready!":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                jet_ready = False
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                jet_ready = False

    #player movement and cotrols
    playerX += playerX_change
    playerY += playerY_change
    
    if playerX < -60:
        playerX = 800
    elif playerX > 800:
        playerX = -60
    elif playerY < -50:
        playerY = 600
    elif playerY >= 590:
        playerY = 590

    #enemy movement and control
    for i in range(num_of_enemies):
        #game over
        end_game = isColision_2(playerX, playerY, enemyX[i], enemyY[i])
        if end_game:
            for j in range(num_of_enemies):
                enemyX[j] = 20000
        if enemyX[i] > 1000:
            game_over()
            break

        #enemy movement
        enemyX[i] += enemyX_change[i]
        if enemyX[i] > 800:
            enemyX_change[i] = -10
            enemyY[i] += 40
        elif enemyX[i] < -60:
            enemyX_change[i] = 10
            enemyY[i] += 40
        elif enemyY[i] > 600:
            enemyY[i] = 0
        # collision!!!!
        colision = isColision(bulletX, bulletY, enemyX[i], enemyY[i])
        if colision:
            num_of_enemies -= 1 
            bulletY = playerY
            bullet_state = "Ready!"
            score += 1
            print(score)
            enemyX[i] = enemyY[i]
            enemyY[i] = enemyY[i]
        enemy(enemyX[i], enemyY[i], i)
        
    #displaying the enemys and ships and bullet
    if bulletY < -3:
        bulletY = playerY
        bullet_state = "Ready!"
        
    if bullet_state == "Fire!":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    if jet_ready:
        jet_fire(playerX, playerY)
        jet_fire_2(playerX, playerY)
    if num_of_enemies == 0:
        win()
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
