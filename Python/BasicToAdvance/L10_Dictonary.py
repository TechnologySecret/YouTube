# Dictionary = A chanable , unordered collection of unique key:value pairs
#             Fast becuase they use hashing, allow use to access a value quickly

capitals = {'USA':'Washington DC', 'India':'New Delhi', 'China': 'Shingia', 'Russia':'Mascow'}

capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()


print(capitals['Germany'])
print(capitals.get('Germany'))
# print(capitals.key())
print(capitals.values())
print(capitals.items())





# for key,value in capitals.items():
#     print(key, value)




