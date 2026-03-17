#1
import shutil
import os

shutil.copy("output.txt", "input.txt")

print("Sucsses")
#2

os.remove("input.txt")

print("succsesfull")
#3

file = "input.txt"

if os.path.exists(file):
    os.remove(file)
    print("Deleted")
else:
    print("notfound")
#4
os.rename("output.txt", "asylym.txt")
#5
os.rmdir("myfolder")