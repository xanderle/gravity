from random import random, randint
import tkinter
from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from disease.cell import Cell
from disease.form import form


class Disease(Model):
    '''
    A 2-Dimensional representation of herd immunity
    '''

    def __init__(self, height, width):
        '''
        Create a new playing area of (height, width) cells.
        '''
        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.

        self.schedule = SimultaneousActivation(self)
        self.noInfected = 0
        self.noVaccinated = 0
        
        # Use a simple grid, where edges wrap around.
        self.grid = Grid(height, width, torus=True)
        self.datacollector = DataCollector(
            {"Infected": lambda m: self.count_type(m, 0),
             "Vaccinated": lambda m: self.count_type(m, 3),
             "Alive": lambda m: self.count_type(m, 1)})
        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.

        for (contents, x, y) in self.grid.coord_iter():
            cell = Cell((x, y), self)
            # if random() < .1:
            #     cell.state = cell.INFECTED
            #     self.noInfected+=1
            # elif random() < .5:
            #     cell.state = cell.VACCINATED
            #     self.noVaccinated +=1
            # else:
                # cell.state = cell.ALIVE
                # self.noAlive+=1
            cell.state = cell.ALIVE

            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)
        # Infect map
        j = 0
        while j <= self.noInfected:
            x = randint(0,width-1)
            y = randint(0,height-1)
            if self.grid[x][y].state == 0:
                continue
            elif self.grid[x][y].state == 3:
                continue
            else:
                self.grid[x][y].state = 0
                j+=1

        # Input vaccinated
        j = 0
        while j <= self.noVaccinated:
            x = randint(0,width-1)
            y = randint(0,height-1)
            if self.grid[x][y].state == 0:
                continue
            elif self.grid[x][y].state == 3:
                continue
            else:
                self.grid[x][y].state = 3
                j+=1
        self.running = True
        self.datacollector.collect(self)
    def step(self):
        '''
        Have the scheduler advance each cell by one step
        '''
        self.schedule.step()
        self.datacollector.collect(self)

    @property
    def Infected(self):
        return self.noInfected
    @staticmethod
    def count_type(model,condition):
        """
        Helper method to count trees in a given condition in a given model.
        """

        count = 0
        for cell in model.schedule.agents:
            if cell.state == condition:
                count += 1
        return count
