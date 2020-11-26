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

backX = 0
backY = 0
backVel = 0

# Tile and Icon
pygame.display.set_caption("Dino Run")
icon = pygame.image.load('base_images/001-dinosaur.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("base_images/dinosaur.png")
playerX = 50
playerY = 480
playerX_change = 0

# Score
score_value = 0
# For any more fonts (https://www.dafont.com/),
# Move downloaded .ttf file to project folder and call it below
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Rectangles used for collisions
player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
test_rect = pygame.Rect(50, 480, 100, 50)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:
    # RGB values for screen
    screen.fill((0, 0, 0))
    # Background image
    if backX == -1920:
        backX = 0

    player_rect.x = playerX
    player_rect.y = playerY

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN - "checks to see if any keyboard key is being pressed"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
                backVel = 2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
                backVel = -2
        # KEYUP - "Checks to see if any key is released (stopped pressing)"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                backVel = 0


    # Incorporate player movement
    playerX += playerX_change
    backX += backVel

    # Show background to screen
    screen.blit(background2, (backX, backY))
    screen.blit(background2, (backX + 1920, backY))
    screen.blit(background3, (backX, backY))
    screen.blit(background3, (backX + 1920, backY))
    screen.blit(background, (backX, backY))
    screen.blit(background, (backX + 1920, backY))
    screen.blit(background1, (backX, backY))
    screen.blit(background1, (backX + 1920, backY))
    screen.blit(background4, (backX, backY))
    screen.blit(background4, (backX + 1920, backY))

    # Show player before foreground
    player(playerX, playerY)
    screen.blit(background5, (backX, backY))
    screen.blit(background5, (backX + 1920, backY))

    # Show score
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)
