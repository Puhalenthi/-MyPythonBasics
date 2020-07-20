import pygame
import random
import time

#Initializing the functions inside pygame
pygame.init()

DX = 600
DY = 600

gameDisplay = pygame.display.set_mode((DX, DY)) #Creating the game window

#Variables to load the image from my computer
ball = pygame.image.load(r'C:\Git\-MyPythonBasics\puhalproject\Cricket\cricketBall.png')
bat1 = pygame.image.load(r'C:\Git\-MyPythonBasics\puhalproject\Cricket\cricketBat.png')
bat2 = pygame.image.load(r'C:\Git\-MyPythonBasics\puhalproject\Cricket\Cricket.png')
clock = pygame.time.Clock()
#First three functions to load the images
def loadbat(x, y):
    gameDisplay.blit(bat1, (x, y))
def loadball(x, y):
    gameDisplay.blit(ball, (x, y))
def loadbat2(x, y):
    gameDisplay.blit(bat2, (x, y))
#Display Player 1's score
def displayScoreP1(scorep1):
    try:
        font = pygame.font.Font('freesansbold.ttf', 25) #Using the font. param: ('font.ttf', size)
        finalScore = 'Yellow Hits: {}'.format(scorep1)
        display = font.render(finalScore, True, (0, 255, 0)) #Making the text displayable. param: (Text, True, (R, B, G))
        gameDisplay.blit(display, (DX - 200, DY - 100)) #Display the text. param: (text, (x, y))
    except:
        pass
def displayScoreP2(scorep2):
    try:
        font = pygame.font.Font('freesansbold.ttf', 25) #Using the font. param: ('font.ttf', size)
        finalScore = 'Black Hits: {}'.format(scorep2)
        display = font.render(finalScore, True, (0, 255, 0)) #Making the text. displayable param: (Text, True, (R, B, G))
        gameDisplay.blit(display, (0, DY - 100)) #Display the tex.t param: (text, (x, y))
    except:
        pass
def displayMissP1(missp1):
    try:
        font = pygame.font.Font('freesansbold.ttf', 25) #Using the font. param: ('font.ttf', size)
        finalMiss = 'Yellow Miss:  {}'.format(missp1)
        display = font.render(finalMiss, True, (255, 0, 0)) #Making the text. displayable. param: (Text, True, (R, B, G))
        gameDisplay.blit(display, (DX - 200, DY - 50)) #Display the text. param: (text, (x, y))
    except:
        pass
def displayMissP2(missp2):
    try:
        font = pygame.font.Font('freesansbold.ttf', 25)
        finalMiss = 'Black Miss:  {}'.format(missp2) #Using the font. param: ('font.ttf', size)
        display = font.render(finalMiss, True, (255, 0, 0)) #Making the text displayable. param: (Text, True, (R, B, G))
        gameDisplay.blit(display, (0, DY - 50)) #Display the text. param: (text, (x, y))
    except:
        pass
def displayTotalBalls(totalBalls):
    try:
        font = pygame.font.Font('freesansbold.ttf', 25) #Using the font param: ('font.ttf', size)
        finalBalls = 'Ball Number:  {}'.format(totalBalls)
        display = font.render(finalBalls, True, (0, 0, 0)) #Making the text displayable. param: (Text, True, (R, B, G))
        gameDisplay.blit(display, (DX / 2 - 125, 500)) #Display the text. param: (text, (x, y))
    except:
        pass
def gameLoop(): #Loop for the game
    #Lines 53 - 67: Variables for the location of the objects and scoring numbers
    bat1x = DX/2 + 50
    bat1y = 0
    bat2x = DX/2 - 50
    bat2y = 0
    ballx = random.randrange(0, DX)
    bally = DY + 10
    changeBat1X = 0
    changeBallY = 0
    changeBat2X = 0
    playing = True
    scorep1 = 0
    scorep2 = 0
    missp1 = 0
    missp2 = 0
    r = 0
    g = 0
    b = 0
    totalBalls = 0
    pygame.display.set_caption('DREAM 11') #Setting the title of the ame window. param: (text)
    #Lines 70 - 76: Using the functions from lines 19 - 50
    displayScoreP1(scorep1)
    displayScoreP2(scorep2)
    displayMissP1(missp1)
    displayMissP2(missp2)
    displayTotalBalls(totalBalls)
    loadbat(bat1x, bat1y)
    loadball(ballx, bally)
    while playing:
        for event in pygame.event.get(): #To check the event
            if event.type == pygame.QUIT: #If you press the X, it will exit the window
                playing = False
                break
            if event.type == pygame.KEYDOWN: #If a key is down:
                if event.key == pygame.K_LEFT: #If the left arrow key is down
                    changeBat1X -= 5
                if event.key == pygame.K_RIGHT: #If the right arrow key is down
                    changeBat1X += 5
                if event.key == pygame.K_a: #If the A key is down
                    changeBat2X -= 5
                if event.key == pygame.K_d: #If the D key is down
                    changeBat2X += 5
            if event.type == pygame.KEYUP: #To check if the keys are not down
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #If the Left and Right arrow keys are not down
                    changeBat1X = 0
                if event.key == pygame.K_a or event.key == pygame.K_d: #If the A or D keys are not down
                    changeBat2X = 0
        # Lines 97 - 99: Adding the changed values
        bat1x += changeBat1X
        bally += changeBallY
        bat2x += changeBat2X
        if changeBallY == 0: #If the Y axis of the ball is changed:
            bally -= 2 #Make the ball go up two
        #Lines 103 - 105: Creating a new image. To show the animation
        loadbat(bat1x, bat1y)
        loadball(ballx, bally)
        loadbat2(bat2x, bat2y)
        if bally < 0: #If the y axis of the ball is less than zero:
            #Lines 108 and 109: Adding a point to the number of missed balls
            missp1 += 1
            missp2 += 1
        if bally < 0 or bally > DY + 50: #If the balls are out of the screen
            ballx = random.randint(1, DX - 50) #Make a new random position for the ball
            bally = DY + 50 #Setting the y location of the ball
            changeBallY = 0 #Resetting the changed y location of the ball
            totalBalls += 1 #Adding one to the number of balls thrown
        pygame.display.flip() #Updating the screen to show new changes
        if bat1y == bally and bat1x - 20 < ballx < ballx + 32 < bat1x + 64: #If the ball touched player one's bat (The yellow one):
            scorep1 += 1 #Adding a point for player one
            missp2 += 1 #Adding one to the number of missed balls for player 2
            changeBallY += 4 #To make the ball go faster after the hit
        if bat2y == bally and bat2x - 20 < ballx < ballx + 32 < bat2x + 64: #If the ball touched player two's bat (The black one):
            scorep2 += 1 #Adding a point for player two
            missp1 += 1 #Adding one to the number of missed balls for player 1
            changeBallY += 4 #To make the ball go faster after the hit
        gameDisplay.fill((r, g, b)) #The color the background. Also to erase the previous loctions of the ball
        if r == 255:
            r = 0
            g += 5
        if g == 255:
            g = 0
            b += 5
        if b == 255:
            b = 0
            r += 5
        #Lines 126 - 130: Using the functions from lines 19 - 50
        displayScoreP1(scorep1)
        displayScoreP2(scorep2)
        displayMissP1(missp1)
        displayMissP2(missp2)
        displayTotalBalls(totalBalls + 1)
        clock.tick(1000) #Setting the speed of the game

print(pygame.colordict)