import os

#1
with open("output.txt", "r") as f:
    print(f.read())
    f.close()
#2
with open("output.txt", "r") as f:
    for i in f:
        print(i.strip())
    f.close()
#3
with open("output.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    f.close()
#4

if os.path.exists("input.txt"):
    with open("input.txt", "r") as f:
        print(f.read())
else:
    print("ERROR")

#5
with open("output.txt", "rb") as f:
    print(f.read()[:10])
    f.close()