# public acces modfire

class PublicAcaccesModfire:
    def __init__(self, first_name, last_name, base_salary, bounse , precentge):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.bounse = bounse
        self.precentge = precentge
    def get_monthly_gross(self):
        return self.base_annual_salary / 12
    
    def get_statered_anual_bounse_amount(self):
         return self.base_annual_salary * (self.bounse_percentage/100)
    
def main ():
    print("hello from main")
    employee1 = PublicAcaccesModfire("kara","smith",1000,2000) # this is public because we can accese it when we do employee1.

if __name__ == "__main__":
    main()





