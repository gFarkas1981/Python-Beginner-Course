# Tuples (immutable lists)

fixlist = ("fixelement1", 'fixelement2', "fixelement3")


# fixlist.append

print(fixlist)

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    newtuple =(*thetuple, value)
    return newtuple

appendtotuple(shoes, "Air max")

# Sets

newset = set(["Spizikes","Air Force 1","Air Force 1","Curry 2","Melo 5"])
# only unique elements
# there is no order in a set

newset.add("Curry 2")

numbers = [3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2]
unique = set(numbers)
