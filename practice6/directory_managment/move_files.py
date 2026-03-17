#1
import shutil
import os

shutil.move("asylym.txt", "file_handling/asylym.txt")

print("File moved!")
#2

dest_folder = "images"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)


shutil.move("output.bin", dest_folder + "/output.bin")
#3
shutil.move("file.txt", "a/b/c/file.txt")