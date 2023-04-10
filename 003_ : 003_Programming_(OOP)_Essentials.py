 #Chapter 3:
#Object-Oriented Programming (OOP) Essentials
class Car:
    # Create a class variable
    NoOfTires = 4
    # creating the class initlizer
    def __init__(self): #without attributes
        self.make = "ford"
        self.model = "moustage"
        self.year = 2010
        self.color = "blue"
        self.MoonRoof = True
        self.EngineRunning = False
    # Method
    def StartTheEngine(self):
        self.EngineRunning = True

    def StopTheEngine(self):
        self.EngineRunning = False
