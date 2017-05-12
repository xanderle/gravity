from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from disease.portrayal import portrayCell
from disease.model import Disease


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, 250, 250)

server = ModularServer(Disease, [canvas_element], "Herd Immunity",
                       50, 50)
