import os

'''

# Q1.  Create a program find a file is avaible or not ?


path = "D:\Learning File\BCA\BCA 1st Sem\PYTHON"

if os.path.exists(path):
    print("That File Locations is exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location is doesn't exists")

    
# Q2: Create a Program move file/folder from or path to another path


source = "Leetcode"
destination = "D:\\Learning File\\BCA\\BCA 1st Sem\\PYTHON\\Leetcode"

try:
    if os.path.exists(destination):
        print("There is a already a file there") 
    else: 
        os.replace(source,destination)
        print(source+"was moved")
except FileNotFoundError:  
    print(source+" was not found") 

    '''

# Q3. Create a program delete a file from source loaction. 

import shutil

path = "riya.t"
try: 
    os.remove(path)  #delete a file
    # os.rmdir(path)  # delete an empty directory
    # shutil.rmtree(path)   #delete a directory containig file

except FileNotFoundError:
     print("That file was not found")
except PermissionError:  
     print("You do not have permission to delete that")
except OSError:
     print("You cannot delete that using that function")
else:
    print(path+"  Delete Done")   # Program Right



