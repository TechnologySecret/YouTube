# filter() = create a collection of elements from an iterables for which a fucntion returns 

# filter(function, iterable)

# Q1. Create a function where 10 friends and diffrent ages 
# but if friends ages is above 18 then drink wine otherwise not
friends = [("Rachel",12),
            ("Monica",17),
            ("Jhone",25),
            ("Zyan",27),
            ("Rock",26),
            ("Markzone",26),
            ("Justin",22),
            ("Lobez",23),
            ("Selena",25),
            ("Gomeza",22)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

print("This is all persons used drinking for party mention below")

for i in drinking_buddies:
    print(i)




