#1
x = lambda a, b : a * b #Multiply argument a with argument b and return the result:
print(x(5, 6))

#2
def myfuc(n):
  return lambda a : a * n #multiply argument a with b and return


mydoubler = myfuc(2) #give a function an argument

print(mydoubler(11))
 
 
#3
def myfuunc(n):
  return lambda a : a * n

mydoubler = myfuunc(2) 
mytripler = myfuunc(3)

print(mydoubler(11))
print(mytripler(11))
#same program but use two functions

#4
def myfunc(a):
    return lambda c : c**a

mypow = myfunc(2)
print(mypow(5))