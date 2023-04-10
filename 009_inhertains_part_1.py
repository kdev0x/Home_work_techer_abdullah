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
        super().__init__(self,first_name,last_name,emp_id,yers_of_exp) # we can add the name of the class yet we added the supper function because when we change the name of the class we dont need to adjust it 1 by 1
        self.annual_salary = annual_salary

     def get_monthly_salary(self):
        return round(self.annual_salary / 12, 2)
     
     def get_annual_bounse(self):
        std_bounse = self.annual_salary * (FullTimeMangmentEmployee.mangment_bounse_precntage / 100)
        exp_bounse = std_bounse * (self.yers_of_exp / 100)
        return std_bounse + exp_bounse



