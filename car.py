class Car:
    def __init__(self, colour, company, speed, model):
        self.colour = colour
        self.company = company
        self.speed = speed
        self.model = model
    
    def start(self):
        print("Started")
    
    def stop(self):
        print("Stop")
    
    def accelerate(self):
        print("Accelerating...")
    
    def gearChange(self):
        print("Gear changed")
    
audi = Car("red", "audi", "100", "audi")
print(audi.colour)
print(audi.start())