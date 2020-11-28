import pygame

from pygame import rect

# Websites used:
# https://www.youtube.com/watch?v=abH2MSBdnWc
# https://www.youtube.com/watch?v=hrQU6zw1vIg&list=PLnqEPPFiEkRfapYiYlfD2pyIYGLyVY2WL&index=8

# Getting a background image
# Make sure image is the same width and height specified by pygame.display.set_mode()


# Clock (frames per second)
clock = pygame.time.Clock();

# Initialize the pygame
pygame.init()

# create the screen (width, height)
screen = pygame.display.set_mode((800, 640))

# Background
# background = pygame.image.load("base_images/background.png")
# Load background images
background = pygame.image.load("Layers/4-BackgroundFar.png").convert_alpha()
background1 = pygame.image.load("Layers/3-BackgroundClose.png").convert_alpha()
background2 = pygame.image.load("Layers/5-Clouds.png").convert_alpha()
background3 = pygame.image.load("Layers/6-Sky.png").convert_alpha()
background4 = pygame.image.load("Layers/2-PlayerLayer.png").convert_alpha()
background5 = pygame.image.load("Layers/1-Foreground.png").convert_alpha()

# Scale down images
background = pygame.transform.scale(background, (1920,640))
background1 = pygame.transform.scale(background1, (1920,640))
background2 = pygame.transform.scale(background2, (1920,640))
background3 = pygame.transform.scale(background3, (1920,640))
background4 = pygame.transform.scale(background4, (1920,640))
background5 = pygame.transform.scale(background5, (1920,640))

# Starting positions for all background layers
backX = 0
backY = 0
backVel = 0
backLayerX = 0
backLayerY = 0
backLayerVel = 0
backFgX = 0
backFgY = 0
backFgVel = 0
# Tile and Icon
pygame.display.set_caption("Dino Run")
icon = pygame.image.load('base_images/001-dinosaur.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("base_images/dinosaur.png")
playerX = 10
playerY = 350
playerX_change = 0
playerY_change = 0

# PlayerAnimation
d1 = pygame.transform.scale(pygame.image.load("Dino/dino1.png"), (250,250))
d2 = pygame.transform.scale(pygame.image.load("Dino/dino2.png"), (250,250))
d3 = pygame.transform.scale(pygame.image.load("Dino/dino3.png"), (250,250))
d4 = pygame.transform.scale(pygame.image.load("Dino/dino4.png"), (250,250))
d5 = pygame.transform.scale(pygame.image.load("Dino/dino5.png"), (250,250))
d6 = pygame.transform.scale(pygame.image.load("Dino/dino6.png"), (250,250))
d7 = pygame.transform.scale(pygame.image.load("Dino/dino7.png"), (250,250))
d8 = pygame.transform.scale(pygame.image.load("Dino/dino8.png"), (250,250))
dinoRun = [d1, d2, d3, d4, d5, d6, d7, d8]
runCount = 0

# Score
score_value = 0
# For any more fonts (https://www.dafont.com/),
# Move downloaded .ttf file to project folder and call it below
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Rectangles used for collisions
player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
# test_rect = pygame.Rect(50, 480, 100, 50)


# Jumping
isJump = False
jumpCount = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def button(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen, ac, (x,y,w,h))
	else:
		pygame.draw.rect(screen, ic, (x,y,w,h))
	#pygame.draw.rect(screen, (210,180,140),(x,10,xLen,yLen))
	smallText = pygame.font.Font('freesansbold.ttf',17)
	textSurf = smallText.render(msg, True, (0,0,0))
	textRect = textSurf.get_rect()
	textRect.center = (x+(w/2), y+(h/2))
	screen.blit(textSurf, textRect)

def show_buttons():
	copperRed = (195, 124, 77)
	lightTan = (235, 204, 171)
	jumpControlBtn = button("Change Jump Control",550,10,200,50,copperRed, lightTan)

def player(x, y):
    global runCount
    
    if runCount == 16:
        runCount = 0
    screen.blit(dinoRun[runCount//2], (x, y))   # divide by 2 so that animation is a little slower
    runCount += 1


# Game loop
running = True
while running:
    pygame.time.delay(30)
    # RGB values for screen
    screen.fill((0, 0, 0))
    # Background image
    if backX == -1920:
        backX = 0
    if backLayerX == -1920:
        backLayerX = 0
    if backFgX == -1920:
        backFgX = 0

    # player_rect.x = playerX
    # player_rect.y = playerY
    #
    # if player_rect.colliderect(test_rect):
    #     pygame.draw.rect(screen, (255, 0, 0), test_rect)
    # else:
    #     pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
        # add animation code?
    else:
        if jumpCount >= -10:
            playerY -= (jumpCount * abs(jumpCount)) * 0.35
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False


        # # KEYDOWN - "checks to see if any keyboard key is being pressed"
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT and player_rect.x > 0 and backX < 0:
        #         playerX_change = -2
        #         backVel = 0.5
        #         backCloseVel = 2
        #     if event.key == pygame.K_RIGHT:
        #         playerX_change = 2
        #         backVel = -0.5
        #         backCloseVel = -2
        #     if not isJump:
        #         if event.key == pygame.K_SPACE:
        #             isJump = True
        # # KEYUP - "Checks to see if any key is released (stopped pressing)"
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         playerX_change = 0
        #         backVel = 0
        #         backCloseVel = 0
        #
        #     if jumpCount >= -10:
        #         playerY -= (jumpCount * abs(jumpCount)) * 0.5
        #         jumpCount -= 1
        #     else:
        #         jumpCount = 10
        #         isJump = False

    backVel = -2
    backLayerVel = -8
    backFgVel = -10

    # Incorporate player movement
    playerX += playerX_change
    backX += backVel
    backLayerX += backLayerVel
    backFgX += backFgVel

    # Show background to screen
    screen.blit(background2, (backX, backY))
    screen.blit(background2, (backX + 1920, backY))
    screen.blit(background3, (backX, backY))
    screen.blit(background3, (backX + 1920, backY))
    screen.blit(background, (backX, backY))
    screen.blit(background, (backX + 1920, backY))
    screen.blit(background1, (backX, backY))
    screen.blit(background1, (backX + 1920, backY))
    screen.blit(background4, (backLayerX, backLayerY))
    screen.blit(background4, (backLayerX + 1920, backLayerY))

    # Show player before foreground
    player(playerX, playerY)
    screen.blit(background5, (backFgX, backLayerY))
    screen.blit(background5, (backFgX + 1920, backLayerY))

    # Show score
    show_score(textX, textY)
    
    # Show buttons
    show_buttons()
    pygame.display.update()

    # clock.tick(60)
