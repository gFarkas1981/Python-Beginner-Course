# Advanced Lists
# Append, Insert, Update, Delete and length

list = ["object1", "object2", "object3", "object4"]

list.append("last one")

list.insert(1, "to the second")

# del(list[3])
list.remove("object3")

list[1] = "object1+"

del(list[-1])

print(list)
print(len(list))
