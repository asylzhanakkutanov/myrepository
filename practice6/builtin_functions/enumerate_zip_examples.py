
#1
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
#2
fruit = ["apple", "banana"]
color = ["red", "yellow"]
for fruit, color in zip(fruit, color):
    print(f"{fruit} is {color}")

#3
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)