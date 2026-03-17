from functools import reduce
#1

numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square)
#2

numberlist = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numberlist))
print(even)
#3

humbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, humbers)
print(total)  
#4
numbers1 = [1, 2, 3, 4, 5]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers1)))
print(even_squares)  

