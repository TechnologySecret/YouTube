# What Does if __name__ == "__main__": Mean?
# In Python, if __name__ == "__main__": is used to ensure that a block of code runs only 
# when the script is executed directly, not when it is imported as a module into another script.

# How to works if_main function 

# Every Python module has a special built-in variable called __name__.
# When a script is executed directly, __name__ is set to "__main__".
# When the script is imported as a module, __name__ is set to the name of the module (not "__main__").
# Using if __name__ == "__main__": ensures that certain code (like test cases or main logic) is executed only 
# when the file is run directly, and not when it is imported.

import L19_DemoFile


# Let's see an example of details 

print("Using Math_Operation module in main.py")
print(f"Add: {L19_DemoFile.add(20,10)}")
print(f"Multiply: {L19_DemoFile.multiply(20,10)}")
