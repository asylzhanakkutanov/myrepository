#python strings
#1
print("Hello")
print('Hello')
#2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#3
a = "Hello"
print(a)

#4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Slicing Strings
#1
b = "Hello, World!"
print(b[2:5])
#2
b = "Hello, World!"
print(b[:5])
#3
b = "Hello, World!"
print(b[2:])
#4
b = "Hello, World!"
print(b[-5:-2])

#Modify Strings
#1
a = "Hello, World!"
print(a.upper())
#2
a = "Hello, World!"
print(a.lower())
#3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#4
a = "Hello, World!"
print(a.replace("H", "J"))
#5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
#1
a = "Hello"
b = "World"
c = a + b
print(c)
#2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format - Strings
#1
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#2
price = 59
txt = f"The price is {price} dollars"
print(txt)
#3
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#4
txt = f"The price is {20 * 59} dollars"
print(txt)

#   escape characters
#1
txt = "We are the so-called \"Vikings\" from the north."
#2
txt = 'It\'s alright.'
print(txt) 

#3
txt = "This will insert one \\ (backslash)."
print(txt) 

#4
txt = "Hello\tWorld!"
print(txt)
#5
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
