from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from portrayal import portrayCell
from model import Disease

from mesa.visualization.modules.TextVisualization import TextElement

class diseaseElement(TextElement):
    '''
    Display a text count of how many happy agents there are.
    '''
    def __init__(self,series):
        self.series = series

    def toPercent(self,total,number):

        return str(round((float(number/total)*100.0),2))
    def render(self, model):
        current_values = []
        self.data_collector_name = "datacollector"
        data_collector = getattr(model, self.data_collector_name)

        for s in self.series:
            name = s["Label"]
            try:
                val = float(data_collector.model_vars[name][-1])  # Latest value
            except:
                val = 0
            current_values.append(val)
        total = sum(current_values)
        string ="                    "
        string +=" Alive: "+self.toPercent(total,current_values[0])+ "%"
        string+= "Infected: "+self.toPercent(total,current_values[1]) + "%"
        string+=" Vaccinated: "+self.toPercent(total,current_values[2])+"%"
        string+=" Immune: "+self.toPercent(total,current_values[3])+"%"
        return string

class placeHolder(TextElement):
    def __init__(self,string):
        self.string = string
    def render(self,model):
        return self.string

class initialStat(TextElement):
    '''
    Display a text count of how many happy agents there are.
    '''
    def __init__(self):
        pass
    def toPercent(self,total,number):
        return str(round((float(number/total)*100.0),2))
    def render(self, model):
        current_values = [model.noAlive,model.noInfected, model.noVaccinated]
        total = sum(current_values)

        string=" Alive: "+self.toPercent(total,current_values[0])+ "%"
        string+= " Infected: "+self.toPercent(total,current_values[1]) + "%"
        string+=" Vaccinated: "+self.toPercent(total,current_values[2])+"%"
        return string

# Make a world that is 100x100, on a 600x600 display.
canvas_element = CanvasGrid(portrayCell, 100, 100, 600, 600)
initialCond = initialStat()
initialText = placeHolder("Initial Percentage")
currentText = placeHolder("Current Percentage")
percentPop = diseaseElement([{"Label": "Alive"},
                          {"Label": "Infected"},
                          {"Label": "Vaccinated"},
                          {"Label": "Immune"}])

chart = ChartModule([{"Label": "Alive", "Color": "green"},
                          {"Label": "Infected", "Color": "red"},
                          {"Label": "Vaccinated", "Color": "blue"},
                          {"Label": "Immune", "Color":"yellow"}])


server = ModularServer(Disease, [canvas_element,chart,initialText,initialCond,currentText,percentPop], "Herd Immunity",
                       100, 100)
server.port=1234
server.launch()
