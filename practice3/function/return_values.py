#1
def pow(x, y):
    return (x+y)**2
#this function will return second power of sums two numbers
res = pow(2, 5)
print(res)
#2
def plus():
    return (12,3,4) # at first this returns a numbers that will be used
x, y, z = plus() # then numbers function will be equal to values
print(x+y+z)

#3
def sum(a, b, /, c): #  before / are positional-only
    return a+b+c
print(sum(5, 4, c = 12))

