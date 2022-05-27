import pygame
import sys

def runGame():
    # Initialize pygame
    pygame.init()

    # Creating the screen
    screen = pygame.display.set_mode((1200, 800))

    # Setting the display caption
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop of the game
    while True:

        # Watch for keyboard and mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible
        pygame.display.flip()

runGame()