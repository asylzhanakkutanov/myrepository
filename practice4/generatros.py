#1

def square_generator(N):
    for i in range(1, N+1):
        yield i ** 2


N = int(input())

gen = square_generator(N)

print()
for num in gen:
    print(num)
"""""
#2
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input())

gen = even_numbers(n)
print(','.join(str(num) for num in gen))
    
#3
n = int(input())

gen = (i for i in range(n) if i % 3 == 0 and i % 4 == 0)

print(', '.join(str(num) for num in gen))
    
    
#4
def squares(a, b):
    for i in range(a, b):
        yield i ** 2


for val in squares(1, 6):
    print(val)
    
#5
n = int(input())

gen = (i for i in range(n, -1, -1))

for num in gen:
    print(num)
    """