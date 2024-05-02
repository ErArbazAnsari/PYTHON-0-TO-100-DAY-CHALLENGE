import time

data = open(
    "./CODE PRACTICE/49_file_handling/myFile.txt", "rb"
)  # here b is binary content, t = text content.
# print(data)

# reading the file
# text = data.read()
# print(text)

# data.close()

# Writing the file
# data = open("this.txt", "a")
# data.write("hrbaz hai")

# content = data.readline()
# print(content)
# data.close()

# appending
# for i in range(0,1000):
#     f = open('./CODE PRACTICE/49_File_Handling/this.txt','a')
#     f.write("Hello")
#     time.sleep(.05)
# f.close()

# Another Way is
with open("./CODE PRACTICE/49_File_Handling/this.txt", "r") as f:
    print(f.readlines())
