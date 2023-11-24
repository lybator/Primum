from Building import GameObject as bui
from Building import *
from Map import map_add_object
class Create:
    def __init__(self, silver:int=0, stone:int=0, wood:int=0):
        self.silver = silver
        self.stone = stone
        self.wood = wood
        self.buildQueue = []
        self.Dominion = []
        self.D_names = []

    def buildQ(self):
        if not self.buildQueue:
            return "There is nothing being buildt."

        if self.buildQueue[0].get_time_to_produce() - 1 == 0:
            self.Dominion.append(self.buildQueue[0])
            self.D_names.append(self.buildQueue.pop(0).get_name())
            return "{0} has been buildt".format(self.Dominion[-1].get_name())

        if self.buildQueue[0].get_time_to_produce() > 0:
            self.buildQueue[0].set_time_to_produce(self.buildQueue[0].get_time_to_produce()-1)
            return "{0} will be buildt in {1} turn(s).".format(
                self.buildQueue[0].get_name(), self.buildQueue[0].get_time_to_produce())

        if self.buildQueue[0].get_time_to_produce() < 0:
            raise Exception(ValueError)


    def create_baracks(self):
        bar = Baracks()
        if (bar.get_cost() <= self.silver):
            self.silver = self.silver - bar.get_cost()
            bar.set_cost(bar.get_cost() + 10)
            self.buildQueue.append(bar)

            return "Barracks is being buildt, the cost is being raised, and a building has been added " \
                   "to the build queue."
        else:
            return "Not enough resources, my liege."


    def create_supply(self):
        sup = Supply()
        if (sup.get_cost() <= self.silver):
            self.silver = self.silver - sup.get_cost()
            self.buildQueue.append(sup)
            sup.set_production(True)
            return "Supply is being buildt, it will provide resources, once buildt."
        else:
            return "Not enough resources my liege, wait few turns until you have enough resources."


    def create_soldier(self):
        sol = Soldier()
        if (sol.get_cost() <= self.silver):
            if 'Barracks' in self.D_names:
                self.silver = self.silver - sol.get_cost()
                self.buildQueue.append(sol)
                return "Barracks are producing your soldiers, my liege"

            else:
                return "You need to create Barracks first my liege"

        return "Not enough resources, my liege"


    def turn_resource_gathering(self):
        for i in self.Dominion:
            if i.get_production() == True:
                self.silver += 5
        return 0

    def gather_resources(self):
        if self.busy == False:
            self.busy = True


