#1
with open("output.txt", "w") as f:
    f.write("Hello ya Asyk iliski\n")
    f.close()
#2
lines = [" 1\n", " 2\n", " 3\n"]

with open("output.txt", "a") as f:
    f.writelines(lines)
    f.close()
#3
name = input()

with open("output.txt", "a") as f:
    f.write(name)
    f.close()
#4
data = "Real."

with open("output.bin", "ab") as f:
    f.write(data.encode("utf-8"))
#5
with open("output.txt", "w") as f:
    for i in range(1, 6, 3):
        f.write(str(i) + "\n")