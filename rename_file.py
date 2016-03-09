import os
def rename_files():
    # Get the list of files
    file_list = os.listdir(r"C:\Users\ramesh\Downloads\prank\prank")
    previous_wd = os.getcwd()
    print("Current Working Directory: " + previous_wd)
    print("Changing to files folder")
    print("Modified current working directory" + os.getcwd())
    os.chdir(r"C:\Users\ramesh\Downloads\prank\prank")

    
    for file_name in file_list:
        print("Old File Name: " + file_name)
        print("New File Name: " + file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))

    os.chdir(previous_wd)
    print("Modiied current working directory" + os.getcwd())
rename_files()
