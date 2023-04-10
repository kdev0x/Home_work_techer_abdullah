   self.EngineRunning = False

class MyCar: #with attrubutes and upgraded
     def __init__(self , make , model , year , color , MoonRoof = False):#(if u want to pass a paramter it has to be in the end if i add a other one it will raise a eror):
        # if you delete the value of the instance variable and make it "" u cant pass objects and when you print it it will be blank
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.MoonRoof = MoonRoof #if you pass true it will be True and if u pass false it will pas true yet if u dont pass anything it will be false because the defult val is false 
        self.EngineRunning =  False
    # Method
    
     def StartTheEngine(self):
        self.EngineRunning = True

     def StopTheEngine(self):
        self.EngineRunning = False
    # destructer this function gets called autmaticly when the objects get deleted
     def __del__(self):
         print("DEstructer invoked".format(self.make, self.model))
        
    
def main():
    print("Hello from the main method") # that is outside the class
    # creating the objects
def car1_create():
    print("Accsesing the car1 variable")
    car1 = MyCar("Ford","mustang",2010,"Blue")
    car2 = MyCar("Tesla,model 3",2020,"Blue", True) 
    model1 = car1.model #the car1.make the "make" is a attribute
    print(model1) # this is a way to accses a attrbiue yet there is a easir way
    #print(car1.model)
    # accesising the car1 attrbiute:
    print(car1.make, car1.model, car1.year, car1.color, car1.MoonRoof )
    del car1
    del car2  # if you tery to do any commands on these var it will be a eror because it is derleted 100%
if __name__ == '__main__':
    main()       
    car1_create()
