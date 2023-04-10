class PayrollProcessor:
   
   def __init__(self, payroll_date):
      self.payroll_date = payroll_date

   def print_payroolrequest(self, list_of_employees):
      print("Payroll Report:{} ".center(50,"-").format(self.payroll_date))#print(formate)

      for emp in list_of_employees:
           print("{}{} : {:.2f}".format(emp.first_name , emp.last_name, emp.get_monthly_salary()))
   def print_annual_bounse(self ,list_of_employees):
      print("Annual Bonuse Report : {}".center(50, "-").format(self.payroll_date))
      for emp in list_of_employees:
           print("{}{} : {:.2f}".format(emp.first_name , emp.last_name, emp.get_monthly_salary()))

class Employee: # we can to reffer to this class base  and parrent class
  def __init__(self,first_name,last_name,emp_id,yers_of_exp):
    self.first_name = first_name
    self.last_name = last_name
    self.emp_id = emp_id
    self.yers_of_exp = yers_of_exp
     
  def get_monthly_salary(self):
     pass
 
  def get_annual_bounse(self):
    pass
 
class FullTimeMangmentEmployee(Employee):
     mangment_bounse_precntage = 20
     def __init__(self,first_name,last_name,emp_id,yers_of_exp, annual_salary): # if you want to add more info you cfan like i will do in the following by adding the instance variable called annual_salary
        super().__init__(first_name,last_name,emp_id,yers_of_exp) # we can add the name of the class yet we added the supper function because when we change the name of the class we dont need to adjust it 1 by 1
        self.annual_salary = annual_salary

     def get_monthly_salary(self):
        return round(self.annual_salary / 12, 2)
     
     def get_annual_bounse(self):
        std_bounse = self.annual_salary * (FullTimeMangmentEmployee.mangment_bounse_precntage / 100)
        exp_bounse = std_bounse * (self.yers_of_exp / 100)
        return std_bounse + exp_bounse


class FullTimeSalryiedEmployee(Employee):
     employee_bounse = 5
     def __init__(self,first_name,last_name,emp_id,yers_of_exp, annual_salary): # if you want to add more info you cfan like i will do in the following by adding the instance variable called annual_salary
        super().__init__(first_name,last_name,emp_id,yers_of_exp) # we can add the name of the class yet we added the supper function because when we change the name of the class we dont need to adjust it 1 by 1
        self.annual_salary = annual_salary

     def get_monthly_salary(self):
        return round(self.annual_salary / 12, 2)
     
     def get_annual_bounse(self):
        emp_std_bounse = self.annual_salary * (FullTimeSalryiedEmployee.employee_bounse / 100)
        emp_exp_bounse = emp_std_bounse * (self.yers_of_exp / 100)
        return emp_std_bounse + emp_exp_bounse


class HourlyContractor(Employee):
     contracter_bounse_precentage = 0.00
     weekly_work_hour = 40
     def __init__(self,first_name,last_name,emp_id,yers_of_exp, hourly_rate): # if you want to add more info you cfan like i will do in the following by adding the instance variable called annual_salary
         super().__init__(self,first_name,last_name,emp_id,yers_of_exp) # we can add the name of the class yet we added the supper function because when we change the name of the class we dont need to adjust it 1 by 1
         self.hourly_rate = hourly_rate

     def get_monthly_sal(self):
        return round((HourlyContractor.weekly_work_hour * 4)* self.hourly_rate)
     
class HourlyEmployee(Employee):
     contracter_bounse_precentage = 2
     weekly_work_hour = 40
     def __init__(self,first_name,last_name,emp_id,yers_of_exp, hourly_rate): # if you want to add more info you cfan like i will do in the following by adding the instance variable called annual_salary
         super().__init__(self,first_name,last_name,emp_id,yers_of_exp) # we can add the name of the class yet we added the supper function because when we change the name of the class we dont need to adjust it 1 by 1
         self.hourly_rate = hourly_rate

     def get_monthly_sal(self):
        std_bounse = (HourlyEmployee.weekly_work_hour * 4) * self.hourly_rate * 12 * (self.employee)
        exp_bounse = std_bounse * (self.yers_of_exp / 100)
        return round((HourlyEmployee.weekly_work_hour * 4)* self.hourly_rate)


class FullTimeSalariedSalesEmployee(FullTimeSalryiedEmployee):
    emp_bounse_precenatge = 3
    weekly_work_hours = 40
    
    def __init__(self,first_name,last_name,emp_id,yers_of_exp , annual_salary , commestion_precntage): 
       super().__init__(first_name,last_name,emp_id,yers_of_exp, annual_salary)
       self.annual_salary = annual_salary
       self.commestion_precntage = commestion_precntage

    def get_monthly_salariyes (self):
       std_bounse = self.annual_salary * (self.yers_of_exp / 100)
       exp_bounse = std_bounse * (self.yers_of_exp)
       return round(std_bounse + exp_bounse)
    


mangment_employee_1 = FullTimeMangmentEmployee("aljawharah","alqhatani", 1001, 5, 1097)
salaried_employee_1 = FullTimeSalryiedEmployee("khalid" , "alqhatani" , 1010, 6 , 12000)
sales_employee_1 = FullTimeSalariedSalesEmployee("sari" , "alqhatani" , 1010, 8, 12000, 5)

list_of_employees = [mangment_employee_1 , salaried_employee_1 , sales_employee_1 ]
payroll = PayrollProcessor("07/01/2023")
payroll.print_payroolrequest(list_of_employees)
