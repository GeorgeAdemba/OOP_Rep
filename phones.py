class phones:
    def __init__(self,name,model,os,storage,ram,battery):
        self.name = name
        self.model = model
        self.os = os
        self.storage = storage
        self.ram = ram
        self.battery = battery

        #display storage and ram details
    def dets(self):
       return "{} {}".format(self.storage, self.ram)
            