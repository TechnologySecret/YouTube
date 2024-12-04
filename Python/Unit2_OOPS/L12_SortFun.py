# sort() method = used with lists
# sort() funcion = used with iterables

students = (("squidward","F",60),
            ("Sandy","A",30),
            ("Patrick","D",36),
            ("Spongebob","A",45),
            ("Mr.Krab","C",78))

age = lambda ages:ages[2]

#students.sort(key = age,reverse = True)
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)