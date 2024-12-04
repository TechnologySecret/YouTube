# Dictionary Comprehsion = create dictionaries using an expression
#                     can replace for loops and certain lambda functions

# Step 1 :- dictionary = {key: expression for (key,value) in iterable}
# Step 2 :- dictionary = {key: expression for (key,value) in iterable if conditional}
# Step 3 :- dictionary = {key: (if/else) for (key,value) in iterable }
# Step 4 :- dictionary = {key: function(value) for (key,value) in iterable }
# -------------------------------------------------------

print("Step 1 Example: :")
# cities_in_F= {'New York': 32, 'Boston': 75, 'Los Angles': 100,'Chicago':50}
# cities_in_C= {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)


# -------------------------------------------------------
print("Step 2 Example: :")

# weather = {'New York': "Snowing",'Boston': "Sunny",'Los Angles':"Sunny",'Chicago':"Cloud"}
# sunny_waehter = {key: value for (key,value) in weather.items() if value == "Sunny"}
# print(sunny_waehter)

# -------------------------------------------------------

# 
print("Step 3 Example: :")

# cities = {'New York':32,'Boston': 75, 'Los Angles': 100,'Chicago':50}
# desc_cities = {key : ("WARM " if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------

print("Step 4 Example: :")

def check_temp(value):
    if value>= 70:
        return "HOT"
    elif 69 >= value >= 40:

        return "WARM"
    else :
        return "COLD"

cities = {'New York':32,'Boston':75,'Los Angles':100, 'Chicago' : 50}
desc_cities = {key:check_temp(value) for (key,value) in cities.items()}
print(desc_cities)





    