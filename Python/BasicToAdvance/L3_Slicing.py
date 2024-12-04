# Slicing String=  Create a substing by extracting elements from another string indexing[] or slice().
#                 [start: stop : step]

name = "Technology Secret"

print ("Using the Slice Method 1:")
s1= slice(3)
s2= slice(1, 3, 7)
s3= slice(-1, -3, -7)

print (name[s1])
print (name[s2])
print (name[s3])

print ("Using the String and List Method 2:")

String = "TECHNOLOGYSECRET"
print (String[:4])  #start and stop methods
print (String[1: 5 : 3])  #start and stop methods and using indexing sequnces sliceing
print (String[ -3: -4: -5])  #Skiping methods in pythons.
print (String[ :: 4])








