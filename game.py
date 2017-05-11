"""
Vaccination Simulation
"""
import time
import pygame
from cell import cell
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
# This sets the number of cells
size = 100
# This is the y height of the array
yheight = size - 1
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(size):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(size):
        grid[row].append(1)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)


cellArray = []
for row in range(size):
    cellArray.append([])
    for column in range(size):
        cellArray[row].append(cell([column,yheight-row]))



grid[1][5] = 3 # INFECTED

cellArray[1][5].infected = True
cellArray[1][5].new = True
# Initialize pygame

pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [size*(HEIGHT+MARGIN)+MARGIN,size*(HEIGHT+MARGIN)+MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
cycles = 100
cycle = 0
# -------- Main Program Loop -----------
while cycle < cycles:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # User clicks the mouse. Get the position
        #     pos = pygame.mouse.get_pos()
        #     # Change the x/y screen coordinates to grid coordinates
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     # Set that location to one
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(size):
        for column in range(size):
            color = WHITE
            if grid[row][column] == 1: ## NOT INFECTED
                color = GREEN
            elif grid[row][column] ==2: ## VACCINATED
                color = BLUE
            elif grid[row][column] == 3: ## INFECTED
                color = RED

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(1)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    for row in range(size):
        for colm in range(size): # Check around and infect
            if(cellArray[row][colm].infected and cellArray[row][colm].new != True): # If cell is infected and not new
                if(row+1 < size):
                    grid[row+1][colm]=cellArray[row+1][colm].infect()
                if(row-1 >=0):
                    grid[row-1][colm]=cellArray[row-1][colm].infect()
                if(colm+1 < size):
                    grid[row][colm+1]=cellArray[row][colm+1].infect()
                if(colm-1 >= 0):
                    grid[row][colm-1]=cellArray[row][colm-1].infect()

    for row in range(size):
        for colm in range(size): # Check around and infect
            cellArray[row][colm].new = False
    cycle+=1

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.

pygame.quit()
