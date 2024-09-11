class vehicle:
    def __init__(self,name,type,price,fuel):
        self.name = name
        self.type = type
        self.price = price
        self.fuel = fuel

    #update price
    def new_price(self,new_price):
        self.price = new_price