import pygame
import time
import random

pygame.init()

bg = (255, 255, 255)

red = (255, 0, 0)

orange = (255, 165, 0)

blue = (0, 0, 255)

green = (0, 255, 0)

black = (0, 0, 0)

DX = 500
DY = 500

screen = pygame.display.set_mode([DX, DY])

screen.fill(bg)

pygame.display.set_caption('Puhal\'s Tron Game')

#hitsound = pygame.mixer.Sound('Users/puhal/Documents/Python/GUI/Snake/hitsound.wav')

pygame.display.flip()

def displayscores(p1score, p2score):
    font = pygame.font.Font('freesansbold.ttf', 25)
    displaystring = 'Player 1 Score was:    {}'.format(p1score)
    display = font.render(displaystring, True, red)
    screen.blit(display, (DX - 400, DY - 150))
    displaystring = 'Player 2 Score was:    {}'.format(p2score)
    display = font.render(displaystring, True, blue)
    screen.blit(display, (DX - 400, DY - 100))


def textdisplay(string, xpos, ypos, color):
    font = pygame.font.Font('freesansbold.ttf', 25)
    displaystring = string
    display = font.render(displaystring, True, color)
    screen.blit(display, (xpos, ypos))

def mainloop():
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        textdisplay('Click Anywhere To Start!', DX - 400, DY - 400, green)
        pygame.display.flip()
        screen.fill(bg)

    done = False
    foreverdone = False
    directionp1 = 'RIGHT'
    directionp2 = 'LEFT'
    tronheadp1x = DX / 4
    tronheadp1y = DY / 2
    tronheadp2x = (DX * 3) / 4
    tronheadp2y = DY / 2
    changetronheadp1x = 0
    changetronheadp1y = 0
    changetronheadp2x = 0
    changetronheadp2y = 0
    p1container = []
    p2container = []
    p1score = 0
    p2score = 0
    p1speed = 1
    p2speed = 1
    nonecounter = 0
    speed1 = False
    speed2 = False
    boostcont1 = []
    boostcont2 = []
    colliding1 = False
    colliding2 = False
    message = ''
    poweruponscreen = False
    speedtimer = 200
    currentspeedtimer = 0
    poweruphitboxx = []
    poweruphitboxy = []
    while foreverdone == False:
        done = False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if directionp1 != 'DOWN':
                            directionp1 = 'UP'
                    if event.key == pygame.K_d:
                        if directionp1 != 'LEFT':
                            directionp1 = 'RIGHT'
                    if event.key == pygame.K_s:
                        if directionp1 != 'UP':
                            directionp1 = 'DOWN'
                    if event.key == pygame.K_a:
                        if directionp1 != 'RIGHT':
                            directionp1 = 'LEFT'
                    if event.key == pygame.K_UP:
                        if directionp2 != 'DOWN':
                            directionp2 = 'UP'
                    if event.key == pygame.K_RIGHT:
                        if directionp2 != 'LEFT':
                            directionp2 = 'RIGHT'
                    if event.key == pygame.K_DOWN:
                        if directionp2 != 'UP':
                            directionp2 = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        if directionp2 != 'RIGHT':
                            directionp2 = 'LEFT'
            

            
            p1container.insert(0, (tronheadp1x, tronheadp1y))
            p2container.insert(0, (tronheadp2x, tronheadp2y))

            if directionp1 == 'UP':
                changetronheadp1y -= p1speed
            if directionp1 == 'RIGHT':
                changetronheadp1x += p1speed
            if directionp1 == 'DOWN':
                changetronheadp1y += p1speed
            if directionp1 == 'LEFT':
                changetronheadp1x -= p1speed
            if directionp2 == 'UP':
                changetronheadp2y -= p2speed
            if directionp2 == 'RIGHT':
                changetronheadp2x += p2speed
            if directionp2 == 'DOWN':
                changetronheadp2y += p2speed
            if directionp2 == 'LEFT':
                changetronheadp2x -= p2speed
            
            tronheadp1x += changetronheadp1x
            tronheadp1y += changetronheadp1y
            tronheadp2x += changetronheadp2x
            tronheadp2y += changetronheadp2y
            
            changetronheadp1x = 0
            changetronheadp1y = 0
            changetronheadp2x = 0
            changetronheadp2y = 0
            
            if tronheadp1x > DX:
                tronheadp1x = 0
            elif tronheadp1x < 0:
                tronheadp1x = 500
            if tronheadp1y > DY:
                tronheadp1y = 0
            elif tronheadp1y < 0:
                tronheadp1y = 500
            
            if tronheadp2x > DX:
                tronheadp2x = 0
            elif tronheadp2x < 0:
                tronheadp2x = 500
            if tronheadp2y > DY:
                tronheadp2y = 0
            elif tronheadp2y < 0:
                tronheadp2y = 500

            if len(p1container) != len(set(p1container)):
                done = True
                message = 'Red hit their own body'
                #pygame.mixer.Sound.play(hitsound)
            if len(p2container) != len(set(p2container)):
                done = True
                message = 'Blue hit their own body'
                #pygame.mixer.Sound.play(hitsound)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    newi1 = tronheadp1x + i
                    newj1 = tronheadp1y + j

                    newi2 = tronheadp2x + i
                    newj2 = tronheadp2y + j
                    if (newi1, newj1) in p2container:
                        done = True
                        message = 'Red hit Blue'
                        #pygame.mixer.Sound.play(hitsound)

                    elif (newi2, newj2) in p1container:
                        done = True
                        message = 'Blue hit Red'
                        #pygame.mixer.Sound.play(hitsound)
            
            for position in range(1, len(p1container)):
                try:
                    x1 = p1container[position][0]
                    y1 = p1container[position][1]
                    body1 = pygame.draw.rect(screen, red, [x1, y1, 5, 5])
                except:
                    pass

            for position in range(1, len(p2container)):
                try:
                    x2 = p2container[position][0]
                    y2 = p2container[position][1]
                    body2 = pygame.draw.rect(screen, blue, [x2, y2, 5, 5])
                except:
                    pass

            if poweruponscreen == False:
                poweruphitboxx = []
                poweruphitboxy = []
                num = random.randint(0, 2)
                powx = random.randint(0, 300)
                powy = random.randint(0, 300)
                for i in range(-10, 11):
                    poweruphitboxx.insert(0, powx + i)
                    poweruphitboxy.insert(0, powy + i)
                poweruponscreen = True

            if num == 0: # BOOST
                pygame.draw.rect(screen, orange, [powx, powy, 5, 5])
            elif num == 1: # REMOVE
                pygame.draw.rect(screen, green, [powx, powy, 5, 5])
            else:
                pygame.draw.rect(screen, black, [powx, powy, 5, 5])

            if tronheadp1x in poweruphitboxx and tronheadp1y in poweruphitboxy and num == 0:
                p1speed = 2
                speed1 = True
                currentspeedtimer = 0
                poweruponscreen = False
                
            elif tronheadp1x in poweruphitboxx and tronheadp1y in poweruphitboxy and num == 1:
                p2container.clear()
                poweruponscreen = False

            elif tronheadp1x in poweruphitboxx and tronheadp1y in poweruphitboxy and num == 2:
                tronheadp2x = random.randint(0, 350)
                tronheadp2y = random.randint(0, 350)
                poweruponscreen = False
                
            elif tronheadp2x in poweruphitboxx and tronheadp2y in poweruphitboxy and num == 0:
                p2speed = 2
                speed2 = True
                currentspeedtimer = 0
                poweruponscreen = False

            elif tronheadp2x in poweruphitboxx and tronheadp2y in poweruphitboxy and num == 1:
                p1container.clear()
                poweruponscreen = False

            elif tronheadp2x in poweruphitboxx and tronheadp2y in poweruphitboxy and num == 2:
                tronheadp1x = random.randint(0, 350)
                tronheadp1y = random.randint(0, 350)
                poweruponscreen = False


            if currentspeedtimer == speedtimer:
                p1speed = 1
                p2speed = 1
                currentspeedtimer = 0
            elif currentspeedtimer < speedtimer:
                if p1speed == 2:
                    p1container.insert(-1, f'None {nonecounter}')
                elif p2speed == 2:
                    p2container.insert(-1, f'None {nonecounter}')

            nonecounter += 1
            currentspeedtimer += 1
            pygame.display.flip()
            screen.fill(bg)
            time.sleep(0.01)

        done = False
        directionp1 = 'RIGHT'
        directionp2 = 'LEFT'
        tronheadp1x = DX / 4
        tronheadp1y = DY / 2
        tronheadp2x = (DX * 3) / 4
        tronheadp2y = DY / 2
        changetronheadp1x = 0
        changetronheadp1y = 0
        changetronheadp2x = 0
        changetronheadp2y = 0
        p1container = []
        p2container = []
        p1speed = 1
        p2speed = 1

        if message.startswith('Red') == True:
            p2score += 1
        elif message.startswith('Blue') == True:
            p1score == 1

        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    foreverdone = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        done = True
            textdisplay('Click To Play Again!', DX - 400, DY - 400, green)
            displayscores(p1score, p2score)
            textdisplay(message, (DX / 2) - 150, (DY / 2) - 50, orange)

            pygame.display.flip()
            screen.fill(bg)
mainloop()
