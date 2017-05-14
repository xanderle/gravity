from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from disease.portrayal import portrayCell
from disease.model import Disease

from mesa.visualization.modules.TextVisualization import TextElement

# Make a world that is 100x100, on a 600x600 display.
canvas_element = CanvasGrid(portrayCell, 100, 100, 600, 600)

chart = ChartModule([{"Label": "Alive", "Color": "green"},
                          {"Label": "Infected", "Color": "red"},
                          {"Label": "Vaccinated", "Color": "blue"},
                          {"Label": "Immune", "Color":"yellow"}])

server = ModularServer(Disease, [canvas_element,chart], "Herd Immunity",
                       100, 100)
server.port=1234
