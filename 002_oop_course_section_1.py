#Chapter 2:
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
 
if __name__ == '__main__':
    main()       
    car1_create()
# create a simple calculater app the with oop
class calc:
    prceantge1 = 110
    prceantge2 = 120
    prceantge3 = 130
    prceantge4 = 140
    prceantge5 = 150
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def addtion(self):
        print(self.num1 + self.num2)
    
    def sub(self):
        print(self.num1 + self.num2)
    
    def mult(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1)

question1 = calc(10,40)
question1.addtion()

#create a project that helps the hr team to  analize a employe bounouse + vaction 
class FinmanceEmployesWage:
    def __init__(self, Base_Salary , bounse_range , vaction , retirment_funds  ):
        self.Base_Salary = Base_Salary
        self.vaction = vaction
        self.retirment_funds = retirment_funds
        self.bounse_range = bounse_range
  
     
    def bounse(self):
        bounses1 = 1 + self.bounse_range / 100
        self.Base_Salary = self.Base_Salary * bounses1
        salary_after_bounse = self.Base_Salary
    def retirment_funds(self):
        if self.retirment_funds == 0:
            pass
        retirment_fund = 1 - self.retirment_funds / 100
        self.Base_Salary = self.Base_Salary * retirment_fund
             
    def print_all(self):
        print("-------------------------------------------------------------------------")
        print("Youre total yearly salary is "+ self.Base_Salary)
        print("Youre vaction for this year is "+ self.vaction)
      
print("                        Yearly Finance")
print("-------------------------------------------------------------------------")
Salary = int(input("Please enter: youre  base salary"))
Bounse = int(input("Please enter: youre anual bounse"))
Vaction = int(input("Please enter: total vaction hours"))
RetirmentFunds = int(input("Please enter: total funds to the retirment funds"))
Year = int(input("how many years you have been working for this company if less then one year enter 0"))

if Salary == 0: 
   print("-------------------------------------------------------------------------")
   raise ValueError("Youre yearly salary shoud be btween 45000 to 125000") 


if Bounse == 0: 
   print("-------------------------------------------------------------------------")
   raise ValueError("Youre yearly bounse shoud be btween 10 to 20 precent") 


if Vaction == 0: 
   print("-------------------------------------------------------------------------")
   raise ValueError("Youre yearly vaction  shoud be atleast  96 hours") 

def vaction_1(vac):
        op1 = 1 + 110 / 100
        vac1 = vac * op1
        return vac1
      
def vaction_2(vac):
        op2 = 1 + 120 / 100
        vac2 = vac * op2
        return vac2
      
     
def vaction_3(vac):
        op3 = 1 + 130 / 100
        vac3 = vac * op3
        return vac3
      
     
    
def vaction_4(vac):
        op4 = 1+ 140 / 100
        vac4 = vac * op4
        return vac4
      

     
def vaction_5(vac):
        op5 =  1 + 150  / 100
        vac5 = vac * op5
        return vac5
      


employee_1 = FinmanceEmployesWage(Salary,Bounse,Vaction,RetirmentFunds)
if Year == 1:
    employee_1.vaction_1(Vaction)
elif Year == 2:
    employee_1.vaction_2(Vaction)
elif Year == 3:
    employee_1.vaction_3(Vaction)
elif Year == 4:
    employee_1.vaction_4(Vaction)
elif Year == 5:
    employee_1.vaction_5(Vaction)

employee_1.bounse()
employee_1.retirment_funds()
employee_1.print_all()



