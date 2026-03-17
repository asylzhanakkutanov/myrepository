import os
#1
os.mkdir("nov_folder")

print("Created")
#2
os.makedirs("nov_folder/nov2/eGov", exist_ok=True)
#3
for item in os.listdir("file_handling"):
    print(item)
#4
path = "gan"

if os.path.exists(path):
    for item in os.listdir(path):
        print(item)
else:
    print("Folder not found")
#5
path1 = "directory_managment"

for item in os.listdir(path1):
    full_path = os.path.join(path1, item)
    print(full_path)