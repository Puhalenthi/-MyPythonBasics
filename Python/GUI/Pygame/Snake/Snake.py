import pygame
import time
import random

pygame.init()

bg = (255, 255, 255)

black = (0, 0, 0)

xcolor = 0
ycolor = 0
zcolor = 0

red = (255, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)

DX = 500
DY = 500


screen = pygame.display.set_mode((DX, DY))

screen.fill(black)

pygame.display.set_caption('Puhal\'s Snake Game')

eatingsound = pygame.mixer.Sound('nom-nom-nom_gPJiWn4.wav')

pygame.display.flip()

def displayscore(score):
    font = pygame.font.Font('freesansbold.ttf', 25)
    stringscore = 'Score: {}'.format(score)
    display = font.render(stringscore, True, green)
    screen.blit(display, ((DX/2) - 50, DY - (DY * 9/10)))

def displayhighscore(context):
    font = pygame.font.Font('freesansbold.ttf', 25)
    HighScores = 'High Scores:\n{}'.format(context)
    display = font.render(HighScores, True, black)
    screen.blit(display, ((DX/2) - 300, DY - 100))

def clickanywhere():
    font = pygame.font.Font('freesansbold.ttf', 25)
    clickanywheretocontinue = 'Click Anywhere To Start!'
    display = font.render(clickanywheretocontinue, True, blue)
    screen.blit(display, ((DX/2) - 150, (DY/2) - 200))

def readhighscore():
    with open('HighScores.txt', 'r') as f:
        context = f.read()
    displayhighscore(context)

def mainloop():
    global xcolor, ycolor, zcolor
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        #readhighscore()
        clickanywhere()
        pygame.display.flip()
    done = False
    snakecontainer = [[DX/2, DY/2]]
    snakecontainerset = set()
    checkcontainer = []
    direction = None
    snakeheadx = DX/2
    snakeheady = DY/2
    changeheadx = 0
    changeheady = 0
    score = 0
    redx = random.randrange(0, DX, 10)
    redy = random.randrange(0, DY, 10)
    pygame.draw.rect(screen, red, [redx, redy, 10, 10])
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if direction != 'DOWN':
                        direction = 'UP'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if direction != 'LEFT':
                        direction = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if direction != 'RIGHT':
                        direction = 'LEFT'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if direction != 'UP':
                        direction = 'DOWN'


        if direction == 'UP':
            changeheady -= 10
        elif direction == 'RIGHT':
            changeheadx += 10
        elif direction == 'LEFT':
            changeheadx -= 10
        elif direction == 'DOWN':
            changeheady += 10

        snakeheadx += changeheadx
        snakeheady += changeheady
        changeheadx = 0
        changeheady = 0

        snakecontainer.insert(0, [snakeheadx, snakeheady])

        del snakecontainer[len(snakecontainer) - 1]

        if snakeheadx > DX - 10:
            snakeheadx = 0
        elif snakeheadx < 0:
            snakeheadx = 500
        if snakeheady > DY - 10:
            snakeheady = 0
        elif snakeheady < 0:
            snakeheady = 500
        
        if redx == snakeheadx and redy == snakeheady:
            redx = random.randrange(0, DX, 10)
            redy = random.randrange(0, DY, 10)
            lastx = snakecontainer[len(snakecontainer) - 1][0]
            lasty = snakecontainer[len(snakecontainer) - 1][1]

            if direction == 'UP':
                lasty += 10
            elif direction == 'RIGHT':
                lastx -= 10
            elif direction == 'LEFT':
                lastx += 10
            elif direction == 'DOWN':
                lasty -= 10
            snakecontainer.append([lastx, lasty])
            score += 1
            pygame.mixer.Sound.play(eatingsound)

        

        for position in range(0, len(snakecontainer)):
            alreadyexists = False
            x = snakecontainer[position][0]
            y = snakecontainer[position][1]
            if snakecontainer[position] not in checkcontainer:
                checkcontainer.append(snakecontainer[position])
            else:
                done = True
                checkcontainer = []
            pygame.draw.rect(screen, (xcolor, ycolor, zcolor), [x, y, 10, 10])
        
        xcolor += 85
        if xcolor == 255:
            xcolor = 0
            ycolor += 85
        if ycolor == 255:
            ycolor = 0
            zcolor += 85
        if zcolor == 255:
            zcolor = 0

        displayscore(score)
        
        checkcontainer = []

        pygame.draw.rect(screen, red, [redx, redy, 10, 10])

        pygame.display.flip()
        screen.fill(black)
        time.sleep(0.1)

mainloop()
