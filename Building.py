class GameObject:
    def __init__(self, name:str="Default_Name", cost:int=0, time_to_produce: int=0,
                 is_alive:bool=False, attacks:bool=False):
        self.name = name
        self.cost = cost
        self.time_to_produce = time_to_produce
        self.is_alive = is_alive
        self.attacks = attacks
        self.icon = 'X'

    def get_name(self):
        return self.name

    def set_name(self, set):
        self.name = set

    def get_cost(self):
        return self.cost

    def set_cost(self, set):
        self.cost = set

    def get_time_to_produce(self):
        return self.time_to_produce

    def set_time_to_produce(self, set):
        self.time_to_produce = set

    def get_is_alive(self):
        return self.is_alive

    def set_is_alive(self, set):
        self.is_alive = set

    def get_attacks(self):
        return self.attacks

    def set_attacks(self, set):
        self.attacks = set

    def get_icon(self):
        return self.icon

    def set_icon(self, set):
        self.icon = set


class Baracks(GameObject):
    def __init__(self):
        super().__init__(name="Barracks", cost=150, time_to_produce=1, is_alive=False, attacks=False)
        self.production = False
        self.icon = 'B'


    def create_unit(self, company_number:int, unit_type:str):
        return "Unit_{0}_created".format(unit_type)


    def get_production(self):
        return self.production


    def set_production(self, set):
        self.production = set


class Supply(GameObject):
    def __init__(self):
        super().__init__(name="Farm", cost=25, time_to_produce=1, is_alive=False, attacks=False)
        self.production = False
        self.icon = 'F'


    def get_production(self):
        return self.production


    def set_production(self, set):
        self.production = set


class Soldier(GameObject):
    def __init__(self):
        super().__init__(name = 'Soldier', cost = 20, time_to_produce = 3, is_alive = True, attacks = True)
        # Company numbers are in hundreds, the 100 is a default number, that allows us to select all units
        self.production = False
        self.busy = False
        self.icon = '^'
        company_number = [100]
        if self.attacks:
            attack_power = 1
        health = 5


    def get_production(self):
        return self.production


    def set_production(self, set):
        self.production = set


    def get_company_number(self):
        return self.company_number


    def set_company_number(self, set):
        self.company_number = [set]


    def get_attack_power(self):
        return self.attack_power


    def set_attack_power(self, set):
        self.attack_power = set


    def get_health(self):
        return self.health


    def set_health(self, set):
        self.health = set


class ResourceNode(GameObject):
    def __init__(self):
        super().__init__(name='TestClass_ResourceNode',cost=-150,time_to_produce=0,is_alive = False, attacks = False)
        self.is_being_mined = False
        self.icon = '$'

    def get_is_being_mined(self):
        return self.is_being_mined

    def set_is_being_mined(self, set):
        self.is_being_mined = set
