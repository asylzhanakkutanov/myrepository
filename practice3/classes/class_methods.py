#1
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b
#Create a method with parameters
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"
#A method that accesses object properties:
p1 = Person("Tobias", 28)
print(p1.get_info())
 
#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"
#With the __str__() method
p1 = Person("Tobias", 36)
print(p1)

#4
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet
#Delete a method from a class
p1.greet() # This will cause an error
