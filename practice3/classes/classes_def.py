class MyClass:
  x = 5 #Create a class named MyClass, with a property named x
#2

p1 = MyClass()
print(p1.x) #Create an object named p1, and print the value of x
#3

p2 = MyClass()
p3 = MyClass()
#Create three objects from the MyClass class
print(p1.x)
print(p2.x)
print(p3.x)

#4
del p1
#Delete the p1 object