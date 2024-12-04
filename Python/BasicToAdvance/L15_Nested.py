# Nested Functions Calls = functions calls inside other functions calls 
                        # inner-most functions calls are resolved first retuned value is used as argument for the next outer function

num = input("Enter a whole positive number:")
num1 = float(num)
num2 = abs(num1)
num3= round(num2)
print(num3)

# print(round(abs(float(input("Enter a whole positive number:")))


