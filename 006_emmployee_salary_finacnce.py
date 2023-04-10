
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



