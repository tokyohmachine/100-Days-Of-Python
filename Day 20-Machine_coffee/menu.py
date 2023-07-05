class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):  # method call init()
        self.name = name  # create attribute call name, cost
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

