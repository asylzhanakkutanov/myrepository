#1
def zhasyn(age): # age is a parameter
  print("YOUR AGE", age)

zhasyn(18) # 18 is an argument
#2
def genius(name, points): #we can give a 2 parameter
  print(name + " " + points)

genius("Asylzhan", "100+") #we must  give a 2 argument

#3
def multip_two():
  return (67, 52)

x, y = multip_two()
print("x:", x*2)
print("y:", y*2)
#this function will return a numbers that multiply by 2

#4
def my_function(a, b, /, *, c, d): #  before / are positional-only, and arguments after * are keyword-only:
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


