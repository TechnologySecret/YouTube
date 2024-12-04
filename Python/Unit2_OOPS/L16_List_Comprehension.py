# list Comprehsion = a way to create a new list with less syntax, 
#                     can mimic certain lambda functions. easier to read. 
#     list = [expression for item in iterable]
#     list = [expression for item in iterable if conditional]
#     list = [expression if/else item in iterable if conditional]

# Example 1: 
squares = []                #create an empty list
for i in range (1, 11):     #create a for loop
    squares.append(i*i)     #define what each loop iteration should do
print(squares)    

print("Step1")  #     list = [expression for item in iterable]

squares = [i*i for i in range (1, 11)]
print(squares)

print("Step2")  #     list = [expression for item in iterable if conditional]

students = [100,90,80,70,60,50,40,30,0]
passed_stud = list(filter(lambda x: x >= 60, students))
print(passed_stud)


print("Step3 ")  #     list = [expression if/else item in iterable if conditional]

# passed_stud = [ i for i in students if i >= 70]  #Reduce methods 
passed_stud = [ i  if i >= 60 else "Failled!!!!" for i in students]  #Reduce methods 
print(passed_stud)





