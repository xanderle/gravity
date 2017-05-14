from mesa import Agent
import random

class Cell(Agent):
    '''Represents a single ALIVE or DEAD cell in the simulation.'''

    INFECTED = 0
    ALIVE = 1
    VACCINATED = 3
    IMMUNE = 2

    def __init__(self, pos, model, init_state=ALIVE):
        '''
        Create a cell, in the given state, at the given x, y position.
        '''
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None
        self.immunityChance = 0.9

    @property
    def isAlive(self):
        return self.state == self.ALIVE
    @property
    def isInfected(self):
        return self.state == self.INFECTED
    @property
    def isVaccinated(self):
        return self.state == self.VACCINATED
    @property
    def isImmune(self):
        return self.state == self.IMMUNE
    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y), True)

    def step(self):
        '''
        Compute if the cell will be dead or alive at the next tick.  This is
        based on the number of alive or dead neighbors.  The state is not
        changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        '''

        # Get the neighbors and apply the rules on whether to be alive or dead
        # at the next tick.
        infected_neighbors = sum(neighbor.isInfected for neighbor in self.neighbors)

        # Assume nextState is unchanged, unless changed below.
        self._nextState = self.state
        if self.isAlive:
            if infected_neighbors > 0:
                chance = random.random()
                if(chance > self.immunityChance):
                    self._nextState = self.IMMUNE
                else:
                    self._nextState = self.INFECTED
        elif self.isVaccinated:
            self._nextState = self.VACCINATED
        elif self.isInfected:
            self._nextState = self.INFECTED
        elif self.isImmune:
            self._nextState = self.IMMUNE
    def advance(self):
        '''
        Set the state to the new computed state -- computed in step().
        '''
        self.state = self._nextState
