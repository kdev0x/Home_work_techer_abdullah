# Random Modules
 the most used function in the random module is caled random 
## example
```python
import random 
print(random.random) 
```
### you can detriment the seed by the seed function 
## example
```python
random.seed(0)
print(random.random) 
```
### now the seed is zero it cant change
### but sometimes i want to chiose a specfice number or word from a list i can use the seed function
  
## example
```python
numbers =  [1,2,3,4]
names = ["khalid","Aljawahrah","sari"]
print(random.choise(numbers))
print(random.choise(names))
```
### yet somtimes i want a charcter from a long string or number from a huge num i can still use the choise func 
## example
```python
random.choise("Iamkhalidandiamsmart")
random.choise(123456789)
```
### the choice function return duplicates yet somtimes you dont wnat that you can use the sample function 
## example
```python 
names = ["khalid","Aljawahrah","sari"]
print(random.sample(names , 2)
```
### this will give me a uniq person 100% and return this in a new list when you add a number larger then the numbers in the list it will return a eror
