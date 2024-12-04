# Scope Variable= The Region that a Variable is recognized, A Varaible is only avaible from inside the region it is created. 
#             A global and localty scoped versions of a vaiable can be created.

name = "Technical"   #global scope (available inside & outside functions)

 
def disp_name():
    name = "Secret"  #local scope (available only isnide this functions)
    print(name)

disp_name()
print(name)


