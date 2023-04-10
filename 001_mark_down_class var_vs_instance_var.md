# Mark down class variable vs instance variable
On `OOP` we use 2 types of variable, `class variable` and `instance variable`
- `Class variable`: Class variable is a variable that gets defined inside the class yet outside of any __init__ function yet we only **define it once** Calling the class variable you need to use the name of the class.
- `Instance variable` is a variable that is defined inside the init function and it is linked with the **self keyword** ontop of that the instance variable get called many times
### example of instance variable and class variable:
```python
#Creating the class
Class Sudent: 
 #Creating the class variable
s1 = Khalid 
def __init__(self , grade , age):
   #Creating the instance variable#
   self.grade = grade
   self. age = age
   
 def print_students(self)
    print("the student name is", Student.s1 , " And his age is" self.age," and his grade is ",self.grade)
    
#Creating the instance - object
k1 = Student(13 , 100)
k1.print_students()
 
