import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()

bg = (255, 255, 255)

green = (0, 255, 0)

red = (255, 0, 0)

yellow = (255, 255, 0)

blue = (0, 0, 255)

lightgreen = (144, 238, 144)

lightred = (255, 114, 118)

lightyellow = (255, 255, 224)

lightblue = (173, 216, 230)

orange = (255, 165, 0)

DX = 400
DY = 500

screen = pygame.display.set_mode([DX, DY])

screen.fill(bg)

pygame.display.set_caption('Puhal\'s Simon Says Game')

pygame.display.flip()

def displayscore():
    font = pygame.font.Font('freesansbold.ttf', 25)
    scoretext = 'Score:  {}'.format(score)
    display = font.render(scoretext, True, orange)
    screen.blit(display, (150, 425))


def mainloop():
    global colors, computercolors, score
    colors = ['GREEN', 'RED', 'YELLOW', 'BLUE']
    done = False
    computercolors = []
    score = 0
    level = 1
    counter = 1
    userlevel = 0
    userturn = False
    lightencolor = None
    pygame.draw.rect(screen, green, [0, 0, 200, 200])
    pygame.draw.rect(screen, red, [200, 0, 200, 200])
    pygame.draw.rect(screen, yellow, [0, 200, 200, 200])
    pygame.draw.rect(screen, blue, [200, 200, 200, 200])
    pygame.display.update()
    time.sleep(0)
    while done == False:
            
        
        displayscore()


        num = random.randint(0, 3)
        color = colors[num]
        computercolors.append(color)
        if level == 1:
            print('First Time Color:', color)
        for lstcolor in computercolors:
            pygame.draw.rect(screen, green, [0, 0, 200, 200])
            pygame.draw.rect(screen, red, [200, 0, 200, 200])
            pygame.draw.rect(screen, yellow, [0, 200, 200, 200])
            pygame.draw.rect(screen, blue, [200, 200, 200, 200])
            
            if lstcolor == 'GREEN':
                pygame.draw.rect(screen, lightgreen, [0, 0, 200, 200])
                pygame.display.update()
                time.sleep(0.5)
                pygame.draw.rect(screen, green, [0, 0, 200, 200])
                pygame.display.update()
                time.sleep(0.5)

            if lstcolor == 'RED':
                pygame.draw.rect(screen, lightred, [200, 0, 200, 200])
                pygame.display.update()
                time.sleep(0.5)
                pygame.draw.rect(screen, red, [200, 0, 200, 200])
                pygame.display.update()
                time.sleep(0.5)

            if lstcolor == 'YELLOW':
                pygame.draw.rect(screen, lightyellow, [0, 200, 200, 200])
                pygame.display.update()
                time.sleep(0.5)
                pygame.draw.rect(screen, yellow, [0, 200, 200, 200])
                pygame.display.update()
                time.sleep(0.5)

            if lstcolor == 'BLUE':
                pygame.draw.rect(screen, lightblue, [200, 200, 200, 200])
                pygame.display.update()
                time.sleep(0.5)
                pygame.draw.rect(screen, blue, [200, 200, 200, 200])
                pygame.display.update()
                time.sleep(0.5)

        userlevel = 0
        print('Level: ', level)
        while userlevel < level:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # GREEN
            if 0 <= mouse[0] < 200 and 0 <= mouse[1] < 200 and click[0] == True:
                if computercolors[userlevel] == 'GREEN':
                    score += 1
                    userlevel += 1
                    print(userlevel)
                    time.sleep(0.3)
                else:
                    done = True
                    quit()
            # RED
            elif 200 <= mouse[0] < 400 and 0 <= mouse[1] < 200 and click[0] == True:
                if computercolors[userlevel] == 'RED':
                    score += 1
                    userlevel += 1
                    print(userlevel)
                    time.sleep(0.3)
                else:
                    done = True
                    quit()
            # YELLOW
            elif 0 <= mouse[0] < 200 and 200 <= mouse[1] < 400 and click[0] == True:
                if computercolors[userlevel] == 'YELLOW':
                    score += 1
                    userlevel += 1
                    print(userlevel)
                    time.sleep(0.3)
                else:
                    done = True
                    quit()
            # BLUE
            elif 200 <= mouse[0] < 400 and 200 <= mouse[1] < 400 and click[0] == True:
                if computercolors[userlevel] == 'BLUE':
                    score += 1
                    userlevel += 1
                    print(userlevel)
                    time.sleep(0.3)
                else:
                    done = True
                    quit()
        userturn = True
        userlevel = 0
        pygame.display.update()
        userturn = False
        level += 1
        screen.fill(bg)
        clock.tick(500)
        


mainloop()