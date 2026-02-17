#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
#Create a class named Person, with firstname and lastname properties, and a printname method
  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#Use the Student class to create an object, and then execute the printname method

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
#Add the __init__() function to the Student class
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#Now we have successfully added the __init__() function, 
# and kept the inheritance of the parent class, 
# and we are ready to add functionality in the __init__() function.

