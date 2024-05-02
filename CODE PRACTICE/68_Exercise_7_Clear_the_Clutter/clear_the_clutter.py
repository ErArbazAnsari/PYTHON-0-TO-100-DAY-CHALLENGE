import os


def changedata(fileextension):
    for i in range(0, 10):
        old_file_path = (
            f"/CODE PRACTICE/68_Exercise_7_Clear_the_Clutter/old files/.{fileextension}"
        )
        new_file_path = f"/CODE PRACTICE/68_Exercise_7_Clear_the_Clutter/new files/{i+1}_file.{fileextension}"
        os.rename(old_file_path, new_file_path)


changedata("txt")
