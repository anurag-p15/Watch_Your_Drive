import pygame
from pygame import mixer
import math
import random

#initialize pygame
pygame.init()
#initialize pygame mixer
pygame.mixer.init()

# Sound
mixer.music.load('Access.wav')
mixer.music.play(-1)

#changing logo image and name of game window and size 

i1=pygame.image.load('window.png')
pygame.display.set_icon(i1)
pygame.display.set_caption("Watch Your Drive!!")
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
playerX = 500
playerY = 634
playerX_change = 0

def player(x, y):
    window.blit(p, (x, y))



#Opposite cars creation
car1 = pygame.image.load('rival.png')
car1X=random.randint(200,236)
car1Y=random.randint(100,200)
car2 = pygame.image.load('rival2.png')
car2X=random.randint(300,336)
car2Y=random.randint(100,200)
car3 = pygame.image.load('rival3.png')
car3X=random.randint(400,436)
car3Y=random.randint(100,200)
car4 = pygame.image.load('rival4.png')
car4X=random.randint(500,536)
car4Y=random.randint(100,200)


def Car(car, x, y):
    window.blit(car, (x, y))

#Collision
def isCollision1(car1X, car1Y, playerX, playerY):
    distance = math.sqrt(math.pow(car1X - playerX, 2) + (math.pow(car1Y - playerY, 2)))
    if distance < 65:
        pygame.mixer.stop()
        return True
    else:
        return False

def isCollision2(car2X, car2Y, playerX, playerY):
    distance = math.sqrt(math.pow(car2X - playerX, 2) + (math.pow(car2Y - playerY, 2)))
    if distance < 65:
        pygame.mixer.stop()
        return True
    else:
        return False

def isCollision3(car3X, car3Y, playerX, playerY):
    distance = math.sqrt(math.pow(car3X - playerX, 2) + (math.pow(car3Y - playerY, 2)))
    if distance < 65:
        pygame.mixer.stop()
        return True
    else:
        return False

def isCollision4(car4X, car4Y, playerX, playerY):
    distance = math.sqrt(math.pow(car4X - playerX, 2) + (math.pow(car4Y - playerY, 2)))
    if distance < 65:
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
    Car(car1,car1X,car1Y)
    Car(car2,car2X,car2Y)
    Car(car3,car3X,car3Y)
    Car(car4,car4X,car4Y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

        ##Condition of ending the game
        collision= isCollision1(car1X, car1Y, playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            game_over_text()
            run=False

        collision= isCollision2(car2X, car2Y, playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            game_over_text()
            run=False

        collision= isCollision3(car3X, car3Y, playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            game_over_text()
            run=False

        collision= isCollision4(car4X, car4Y, playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            game_over_text()
            run=False 

        # if keystroke is pressed check whether its right or left (Player Movement)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -30
            if event.key == pygame.K_RIGHT:
                playerX_change = 30
            
                
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        playerX += playerX_change  
        if playerX < 200  or playerX > 536:
            pygame.mixer.stop()
            game_over_text() 
            run=False
        
        #Condition of moving incoming cars 
        car1Y+=20
        car2Y+=15
        car3Y+=20
        car4Y+=30
        
        if car1Y > 764:
           car1Y = -100
           score_value+=1
        if car2Y > 764:
           car2Y = -100
           score_value+=1
        if car3Y > 764:
           car3Y = -100
           score_value+=1
        if car4Y > 764:
           car4Y =-100
           score_value+=1
        


    show_score(textX, testY)
    pygame.display.update()  


    
    
    
        