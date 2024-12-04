# zip (* iterables) :-  aggregate elements from two or more iterables(list,tuples, set, etc)
                    # :- Create a zip object paired elements stored in tuples for each elements.

usernames = ["Shailesh","Rose","Relationship"]
passwords= ("p@ssword","love","together")
login_update = ["1/2/2002","12/19/2005","11/30/2024"]

users = zip(usernames,passwords,login_update)

for i in users: 
    print(i)
