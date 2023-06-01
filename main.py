from numpy import append
import pygame
from pygame import mixer
import math
import random

#initialize pygame
pygame.init()
#initialize pygame mixer
pygame.mixer.init()

# Sound
mixer.music.load('Prodigy.wav')
mixer.music.play(-1)

#changing logo image and name of game window and size 

window=pygame.display.set_mode((800,700))

# Background
background = pygame.image.load('background.png')

#Show Score of player:

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 0, 0))
    window.blit(score, (x, y))
score_value=0

#Quit Display
over_font = pygame.font.Font('freesansbold.ttf', 72)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 255))
    window.blit(over_text, (150, 250))

#Player Creation
p=pygame.image.load('player.png')
pygame.display.set_icon(p)
playerX = random.randint(200,560)
playerY = 634
playerX_change = 0

def player(x, y):
    window.blit(p, (int(x), int(y)))



#Opposite cars creation
CarImg=[]
CarX=[]
CarY=[]
num_of_cars=5
CarY_change = [0]*num_of_cars
for i in range(num_of_cars):
    if i%5==0:
        CarImg.append(pygame.image.load('rival.png'))
        CarX.append(random.randint(200,250))
        CarY.append(random.randint(100,200))
    if i%5==1:
        CarImg.append(pygame.image.load('rival 2.png'))
        CarX.append(random.randint(280,330))
        CarY.append(random.randint(100,200))
    if i%5==2:
        CarImg.append(pygame.image.load('rival.png'))
        CarX.append(random.randint(360,410))
        CarY.append(random.randint(100,200))
    if i%5==3:
        CarImg.append(pygame.image.load('rival 2.png'))
        CarX.append(random.randint(440,490))
        CarY.append(random.randint(100,200))
    if i%5==4:
        CarImg.append(pygame.image.load('rival.png'))
        CarX.append(random.randint(520,550))
        CarY.append(random.randint(100,200))


def Car(CarImg, x, y):
    window.blit(CarImg, (x, y))

#Collision
def isCollision(carX, carY, playerX, playerY):
    distance = math.sqrt(math.pow(carX - playerX, 2) + (math.pow(carY - playerY, 2)))
    if distance < 35:
        pygame.mixer.stop()
        return True
    else:
        return False

##GAME LOOP
run=True
while run:
    window.fill((34,139,34))
    window.blit(background,(200,0))
    #Creation of players and down cars
    player(playerX,playerY)
    for i in range(num_of_cars):
        Car(CarImg[i], CarX[i], CarY[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for i in range(num_of_cars):
                    if i%5==0:
                        CarY[i]+=1.3
                    if i%5==1:
                        CarY[i]+=1.5
                    if i%5==2:
                        CarY[i]+=1.4
                    if i%5==3:
                        CarY[i]+=1.2
                    if i%5==4:
                        CarY[i]+=1.3 
        ##Condition of ending the game
    for i in range(num_of_cars):
        collision= isCollision(CarX[i], CarY[i], playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            game_over_text()
            run=False
        

        # if keystroke is pressed check whether its right or left (Player Movement)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
                playerX_change = -2.5 
        if event.key == pygame.K_RIGHT:
                playerX_change = 2.5        
                
    if  event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    playerX += playerX_change  
        
    if score_value>10:
        t=int(score_value/10)
        n=5
        for i in range(n):
             if i%5==0:
                CarY[i]=CarY[i]+(0.4*t)
            if i%5==1:
                CarY[i]=CarY[i]+(0.5*t)
            if i%5==2:
                CarY[i]=CarY[i]+(0.7*t)
            if i%5==3:
                CarY[i]=CarY[i]+(0.5*t)
            if i%5==4:
                CarY[i]=CarY[i]+(0.6*t)
    if playerX < 200  or playerX > 590:
        pygame.mixer.stop()
        for i in range(n):
            CarX[i]=900 
            CarY[i]=900
            game_over_text()  
            run=False
    n=5
    for i in range(n):
        if(i%5==0):
                if CarY[i] > 700:
                    CarY[i] = -100
                    CarX[i]=random.randint(200,250)
                    score_value+=1
        if(i%5==1):
            if CarY[i] > 700:
                CarY[i] = -100
                CarX[i]=random.randint(280,330)
                score_value+=1
        if(i%5==2):
            if CarY[i] > 700:
                CarY[i] = -100
                CarX[i]=random.randint(360,410)
                score_value+=1
        if(i%5==3):
            if CarY[i] > 700:
                CarY[i] = -100
                CarX[i]=random.randint(440,490)
                score_value+=1
        if(i%5==4):
            if CarY[i] > 700:
                CarY[i] = -100
                CarX[i]=random.randint(520,550)
                score_value+=1
    show_score(textX, testY)
    pygame.display.update()  

##Ending the game
pygame.quit()
