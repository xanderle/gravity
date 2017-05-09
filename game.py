"""
Dust
"""
import random
import pygame
import numpy as np
from dust import dust
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5
size = 10

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = np.zeros(shape=(size,size))

dustArray = []

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(HEIGHT+MARGIN)*size, (HEIGHT+MARGIN)*size]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## Populate map with dust
j = 0
while j <= 10:
    x = random.randint(0,size-1)
    y = random.randint(0,size-1)
    print(x,y)
    if grid[size-y-1][x] == 1:
        continue
    else:
        grid[size-y-1][x] = 1
        dustArray.append(dust(x,y))
        j+=1

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(size):
        for column in range(size):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
    for dust in dustArray:
        grid[size-dust.y-1][dust.x] == 0
        print(dust.y)
        dust.move()
        print(dust.y)
        if(size - dust.y - 1 <= 0):
            dust.y = 0
        if(size - dust.x -1 <= 0):
            dust.x = 0
        else:
            grid[size-dust.y-1][dust.x] = 1
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
