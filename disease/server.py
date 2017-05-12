from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from disease.portrayal import portrayCell
from disease.model import Disease


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 100, 100, 600, 600)

tree_chart = ChartModule([{"Label": "Alive", "Color": "green"},
                          {"Label": "Infected", "Color": "red"},
                          {"Label": "Vaccinated", "Color": "blue"}])

server = ModularServer(Disease, [canvas_element,tree_chart], "Herd Immunity",
                       100, 100)
