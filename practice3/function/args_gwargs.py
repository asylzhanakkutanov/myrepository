#1
def my_function(*args): #The *args parameter allows a function to accept any number of positional arguments.
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
#Inside the function, args becomes a tuple containing all the passed arguments:
my_function("Asik", "Era", "Beka")

#2
def names(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
names(**person) #If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

#3
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args) #shows that Asik and Alek is a positional arguments
  print("Keyword arguments:", kwargs) # shows that age = 25, city = "Oslo" is keyword arguments

my_function("User Info", "Asik", "Alek", age = 25, city = "Oslo")

#4
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Asylznab", lname = "Akkutanov")
