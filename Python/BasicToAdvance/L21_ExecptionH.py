# Exception" = events detected during that interrupt the flow of a program.

try : 
    numerator = int(input("Enter a number to divide:"))
    denominator = int (input("Enter a number to divide by: "))
    result= numerator/denominator

except ZeroDivisionError as e: 
    print(e)
    print("You can't divide bt zero! idiot!!")
except ValueError as e: 
    print(e)
    print("Enter only numbers pls")
except Exception as e:  
    print(e)
    print("Something went wrong")
else : 
    print(result)
finally: print("That will always execute")
    