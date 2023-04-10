
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
