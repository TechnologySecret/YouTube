# File Handling: It means access a specific file and folded from your directory. 

# Example 1: Read Mode  and closed file

# with open('pytest.txt') as file:
#     print(file.read())     #Note:  No Defined any specfic location about file.. 
# print(file.closed)

# EXample 2" Generate Error when open file  
# try :
#     # with open('test.txt') as file:
#     with open('pytest.txt') as file:
#         print(file.read())
#         print(" Location Found Successful")
# except FileNotFoundError:  
#     print("That file was not found")

# Example 3: Write in something content file.|| Over Write. 

# text = '''Hi,This test write by File No 
#         23> and \n Example 3 > Well  
#         You are successfully write ur content.
#         But this is over write file handing topics'''

# with open('pytest.txt','w') as file:    # 'w' Write:- Using Write text but overwrite
# # with open('pytest.txt','a') as file:    # 'a' Append :- Using Write text not overwrite
#     file.write(text)


# Example 4:  File Copy and Paste   from Destination 
# copyfile() =copies content of a file

# copy()  = copyfile() + permission mode + destination can be a directory 
# copy2() = copy + copies metadata(file's creation and midification times)

import shutil 
shutil.copy2('test.txt','D:\Learning File\BCA\BCA 1st Sem\PYTHON')   #src.dst

