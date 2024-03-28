# with open("CODE PRACTICE/51_seet()_tell()_in_python/file.txt", "r") as f:
#     # f.read('file.txt')
#     print(type(f))
#     f.seek(5)
#     data = f.read(3)
#     print(data)

#     print(f.tell())

with open("CODE PRACTICE/51_seet()_tell()_in_python/file2.txt", "w") as f:
    f.write("Hello, World")
    print(type(f))
    f.truncate(5)  # Maximum character limit=5
