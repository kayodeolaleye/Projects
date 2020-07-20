"""
A simple game built with [PyGame](https://www.pygame.org/)

Author: Kayode Olaleye
Contact: kaykola.olaleye@gmail.com
Date: 2020

Disclaimer:
The code is written purely just to practice building games. 
It is not written with optimality in mind. Please feel free to suggest
ways of improving it. 

Dependencies: 
- Python 3.7.6 or later. You can download the latest version here => https://www.python.org/downloads/
- pygame => https://www.pygame.org/wiki/GettingStarted

Images by:
- https://pixabay.com/users/thedigitalartist
- https://pixabay.com/users/openclipart-vectors
- https://pixabay.com/users/openclipart-vectors
- https://pixabay.com/users/openclipart-vectors
- https://pixabay.com/users/davidrockdesign
- https://pixabay.com/users/davidrockdesign

Running code from a Linux terminal terminal: 
- cd to the folder containing sample_game.py
- type the command => python sample_game.py

"""

import pygame
import random 

pygame.init() # initialise pygame

# CONSTANTS

# window size
WIN_WIDTH = 1040 # The width of the window
WIN_HEIGHT = 680 # The height of the window

# RGB value for white, green, and red colour
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# text surface size
X = 400
Y = 400

# Create the game's window with width SCREEN_WIDTH and height SCREEN_HEIGHT

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Create the surface where text messages will be displayed with width X and height Y
# display_surface = pygame.display.set_mode((X, Y))

# Set the pygame window name
pygame.display.set_caption("A Simple Game")

# Manage the rendering style of text that will be displayed when the game ends

font = pygame.font.Font("freesansbold.ttf", 32) # create a font object. pygame.font.Font(font-file, size-of-the-font).
winning_text = font.render("You Win!", True, GREEN) # this text will be displayed if the player won.
losing_text = font.render("You Lose!", True, RED) # this text will be displayed if the player lost.

# create a rectangular object for the text surface

# textWinningRect = winning_text.get_rect() 
# textLosingRect = losing_text.get_rect()

# Set the centre of the rectangular object
textWinningRect = (X // 3, Y // 3)
textLosingRect = (X // 3, Y // 3)

# Create the player, enemies, and prize variables and assign them the images the in the images folder

player = pygame.image.load("images/player.png") 
player = pygame.transform.scale(player, (120, 130)) # scale image to a smaller size
enemy1 = pygame.image.load("images/enemy1.png")
enemy1 = pygame.transform.scale(enemy1, (120, 130))
enemy2 = pygame.image.load("images/enemy2.png")
enemy2 = pygame.transform.scale(enemy2, (120, 130))
enemy3 = pygame.image.load("images/enemy3.png")
enemy3 = pygame.transform.scale(enemy3, (120, 130))
prize = pygame.image.load("images/prize.png")
prize = pygame.transform.scale(prize, (120, 130))

# Declare variables to store the position of the player, enemies, and prize

playerXPosition = 100
playerYPosition = 50

# Make the enemies start off screen and at a random x or y position

enemy1XPosition = WIN_WIDTH
enemy1YPosition = random.randint(0, WIN_HEIGHT - enemy1.get_height() // 4)

enemy2XPosition = WIN_WIDTH 
enemy2YPosition = random.randint(0, WIN_HEIGHT - enemy2.get_height() // 2)

enemy3XPosition = WIN_WIDTH // 4
enemy3YPosition = random.randint(0, WIN_HEIGHT - enemy3.get_height() // 4)

prizeXPosition = WIN_WIDTH // 2
prizeYPosition = WIN_HEIGHT

# Declare boolean variables for the keyboard events and set them to False

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# We need a while loop to make the game's window active and visible until an keyboard even is triggered

run = True
while run:
    win.fill(0) # Clears the window
    # Draw the player, enemies and prize image to the window at the specified positions
    win.blit(player, (playerXPosition, playerYPosition)) 
    win.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    win.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    win.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    win.blit(prize, (prizeXPosition, prizeYPosition))

    # update the window
    pygame.display.flip()

    # Loop through events in the game.

    for event in pygame.event.get():

        # Check if the user quits the program, then if so, it exits the game.
        if event.type == pygame.QUIT:
            # pygame.quit()
            # # exit(0)
            run = False

        # Check if the user press a key down
        if event.type == pygame.KEYDOWN:

            # Check if the key pressed is the one we want.

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # Check if a key is not pressed by the user.

        if event.type == pygame.KEYUP:

            # Check if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
        

    # Handle the movement of the player object within the window

    if keyUp == True:
        
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown == True:
        if playerYPosition < WIN_HEIGHT - player.get_height(): # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player beyond the window's left width.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < WIN_WIDTH - player.get_width(): # This makes sure that the user does not move the player beyond the window's right width.
            playerXPosition += 1


    # Enclose the player, enemies and prize in  bounding boxes. This allows to check for collisions between the player and enemies and between the player and the prize

    playerBox = pygame.Rect(player.get_rect())

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy3Box = pygame.Rect(enemy3.get_rect())

    prizeBox = pygame.Rect(prize.get_rect())

    # Update the playerBox position to the player's position. Do the same for the enemy{1,2,3}Box and the prizeBox

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the bounding boxes

    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        # Create the surface where text messages will be displayed with width X and height Y
        display_surface = pygame.display.set_mode((X, Y))
        win.fill(WHITE)
        # display_surface.fill(WHITE) # Completely fill the surface object with white colour
        win.blit(losing_text, textLosingRect) # Copy the losing text message to the center of the display surface
        # update the window
        pygame.display.flip()
        run = False
    
    if playerBox.colliderect(prizeBox):

        display_surface = pygame.display.set_mode((X, Y))
        display_surface.fill(WHITE) 
        display_surface.blit(winning_text, textWinningRect) 
        pygame.display.flip()
        run = False

    # If all the enemies are off the screen, the player wins the game:

    if enemy1XPosition < 0 - enemy1.get_width() and enemy2XPosition < 0 - enemy2.get_width() and enemy3YPosition < 0 - enemy3.get_width():
        display_surface = pygame.display.set_mode((X, Y))
        display_surface.fill(WHITE) 
        display_surface.blit(winning_text, textWinningRect) 
        pygame.display.flip()
        run = False
        

    
    # Make the enemies approach the player.

    enemy1XPosition -= 0.45
    enemy2XPosition -= 0.45
    enemy3YPosition -= 0.45
    prizeYPosition -= 0.12

    
        




