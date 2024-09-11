class food:
    def __init__(self,name,type,calories,quantity):
        self.name = name
        self.type = type
        self.calories = calories
        self.quantity = quantity

    #updating quantity of food
    def new_quantity(self,new_quantity):
        self.quantity = new_quantity
        
    #updating calories of food
    def new_calories(self,new_calories):
        self.calories = new_calories
