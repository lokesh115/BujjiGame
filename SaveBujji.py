import pygame
import random
pygame.init()

win = pygame.display.set_mode((728,455))

pygame.display.set_caption("Save Bujji")

bg = pygame.image.load('assets/bg.jpg')

# Load and play music
pygame.mixer.music.load("assets/Bujji Theme.mp3")  # Path to your music file
pygame.mixer.music.set_volume(0.5)          # Volume (0.0 to 1.0)
pygame.mixer.music.play(-1) 

class GameConfig:    
    x = 50
    y = 50

    width = 60
    height = 60
    vel = 10
    stack_limit = 5
    stack = []
    font = pygame.font.SysFont('comicsans', 30, True)
    midfont = pygame.font.SysFont('comicsans', 90, True)
    bigfont = pygame.font.SysFont('comicsans', 90, True)
    run = True
    k = 0

gameConfig = GameConfig()


color_collect = []
color_space = [(77,137,99),(225,179,120),(159,2,81),(163,214,245),(238,50,51),(108,116,118),(33,182,168),(127,84,23)]
iter = 5
while iter > 0:
    ind = random.randrange(0,4)
    color_collect.append(color_space[ind])
    color_space.pop(ind)
    iter -= 1
def color_change():
    gameConfig.k = random.randrange(0,5)

def game_over_won():
    win.blit(bg, (0,0))
    win.blit(gameConfig.bigfont.render('You Won!!!', 1, (255,255,255)), (320, 222))
    
    #for i in stack:
            #pygame.draw.rect(win, i[2], (i[0],i[1],width, height))
    
    pygame.display.update()
    pygame.time.delay(5000)


def redrawGameWindow():
    win.blit(bg, (0,0))
    win.blit(gameConfig.font.render('Target : ', 1, (255,255,255)), (140, 378))
    for i in range(5):
        pygame.draw.rect(win, color_collect[i], (244+gameConfig.width*i,360,gameConfig.width, gameConfig.height))
    pygame.draw.rect(win, (0,0,0), (300,100,2*gameConfig.width, gameConfig.height))
    pygame.draw.rect(win, (248,228,204), (300,250,5*gameConfig.width, gameConfig.height))
    stack_text = gameConfig.font.render('STACK', 1, (219,173,114))
    win.blit(stack_text, (375, 270))
    if len(gameConfig.stack)!=0:
        for i in gameConfig.stack:
            pygame.draw.rect(win, i[2], (i[0],i[1],gameConfig.width, gameConfig.height))
    text = gameConfig.font.render('Discard', 1, (255,255,255))
    win.blit(text, (315, 120))
    pygame.draw.rect(win, color_collect[gameConfig.k], (gameConfig.x,gameConfig.y,gameConfig.width, gameConfig.height))
    pygame.display.update()

def runGameLogic():
    if gameConfig.x == 300 and gameConfig.y == 100:
        gameConfig.x,gameConfig.y = 50,50
        gameConfig.k = random.randrange(0,5)
    if gameConfig.x == 300+(gameConfig.stack_limit-1)*gameConfig.width and gameConfig.y == 250:
        #pygame.draw.rect(win, color_collect[k], (300+(stack_limit-1),250,width, height))
        if gameConfig.k != 5 - gameConfig.stack_limit:
            win.blit(bg, (0,0))
            win.blit(gameConfig.bigfont.render('You Lost!', 1, (255,255,255)), (320, 222))
            pygame.display.update()
            #win.fill(0,0,0)
            pygame.time.delay(5000)
            
            gameConfig.run = False
        elif gameConfig.stack_limit == 1:
            gameConfig.stack_limit -= 1
            gameConfig.stack.append((gameConfig.x,gameConfig.y,color_collect[gameConfig.k]))
            pygame.time.delay(1200)
            game_over_won()
            gameConfig.run = False
        gameConfig.stack_limit -= 1
        gameConfig.stack.append((gameConfig.x,gameConfig.y,color_collect[gameConfig.k]))
        gameConfig.k = random.randrange(0,4)
        gameConfig.x,gameConfig.y = 50,50

win.blit(bg, (0,0))
win.blit(gameConfig.midfont.render('Instructions', 1, (255,255,255)), (130, 45))
win.blit(gameConfig.font.render('Arrange the coloured boxes in the stack such that when ', 1, (255,255,255)), (40, 168))
win.blit(gameConfig.font.render('all the boxes are popped out of the stack the resulting ', 1, (255,255,255)), (45, 195))
win.blit(gameConfig.font.render('order must be similar to that of the "Target" given', 1, (255,255,255)), (65, 222))
win.blit(gameConfig.font.render('Discard the unnecessary blocks', 1, (255,255,255)), (170, 277))
win.blit(gameConfig.font.render('Press SPACE to start', 1, (0,0,0)), (230, 400))


pygame.display.update()
pygame.time.delay(1000)
startGame = False
while gameConfig.run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameConfig.run = False

    keys = pygame.key.get_pressed()

    runGameLogic()

    if keys[pygame.K_SPACE]:
        startGame = True
    if keys[pygame.K_LEFT] and gameConfig.x > gameConfig.vel:
        gameConfig.x -= gameConfig.vel
    if keys[pygame.K_RIGHT] and gameConfig.x < 758-gameConfig.vel-gameConfig.width:
        gameConfig.x += gameConfig.vel
    if keys[pygame.K_UP] and gameConfig.y > gameConfig.vel:
        gameConfig.y -= gameConfig.vel
    if keys[pygame.K_DOWN] and gameConfig.y < 455-gameConfig.vel-gameConfig.height:
        gameConfig.y += gameConfig.vel
    if startGame:
        redrawGameWindow()
pygame.quit()