# str.format()  = It is optional methods that gives user more control when displaying output.

# 1st Example of String:  
'''
channel = "Technology"
name= "Secret" 

# print("The"+ channel+ "Sharing Information" + name)
# print("The {}  Sharing Information {} ".format(channel,name))
# print("The {1}  Sharing Information {0} ".format(channel,name))   #Positional Arguments
print("The {channel}  Sharing Information {channel} ".format(channel="Technology",name="Secret"))   #Keywords Arguments

text = "The {} Shairing Informationa {} " 
print(text.format(channel,name))
''' 

# 2nd Example of String with hiden Space:
'''
name= "Shailesh"

print("Hello My Name is {}".format(name))
print("Hello My Name is {:10} Nice to meet you Mr.. ".format(name))   #:10 __ Include 10 Space between is............meets
print("Hello My Name is {:<10} Nice to meet you Mr.. ".format(name))
print("Hello My Name is {:>10} Nice to meet you Mr.. ".format(name))
print("Hello My Name is {:^10} Nice to meet you Mr.. ".format(name))

'''


# 3rd Example of Basic Number:

num= 101 
print("The Number pi i {:.3f}" .format(num))
print("The number is {:,}".format(num))
print("The number is {:b}".format(num))  #Binary
print("The number is {:o}".format(num))  #Octal 
print("The number is {:x}".format(num))  #HexaDecimal
print("The number is {:e}".format(num))  # Sectific Number


