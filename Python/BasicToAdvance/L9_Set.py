# Set=  Set id Collection which is uno.rdered, unindeded. No duplicate values

untensils = {"fork", " spoon","knife"}
dishes = {"bowl", "plate", "cup","plate","knife"}

# untensils.add("napkin")
# untensils.remove("fork")
# untensils.clear()
# dishes.update(untensils)
dinner_table = untensils.union(dishes)

for x in dinner_table:
    print(x)

print(untensils)
print(untensils.difference(untensils))
print(untensils.intersection(dishes))
