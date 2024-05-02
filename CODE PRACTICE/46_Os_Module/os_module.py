import os

# if(not os.path.exists("Arbaz")):
#     os.mkdir("Arbaz")

# for i in range(0,1000):
#     os.mkdir(f"Arbaz/{i+1}_Folder")

# for i in range(0,1000):
#     os.rename(f"Arbaz/{i+1}_Folder", f"Arbaz/{i+1}_FolderName")


# folders = os.listdir("Arbaz")
# print(folders)

# for folder in folders:
#     print(folder, end=" ")
#     print(os.listdir(f"Arbaz/{folder}"))

print(os.getcwd())
os.chdir("C:")
print(os.getcwd())

## Do Refer : https://docs.python.org/3/library/os.html#module-os
